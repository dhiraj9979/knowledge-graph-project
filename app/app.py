import spacy
from neo4j import GraphDatabase
from py2neo import Graph
from langchain.document_loaders import PyPDFLoader

# Step 1: Define Neo4j Connection
class Neo4jKnowledgeGraph:
    def __init__(self, uri, username, password):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))
        self.graph = Graph(uri, auth=(username, password))  # This is for py2neo visualization

    def close(self):
        self.driver.close()

    def create_entity(self, entity_name, entity_type):
        with self.driver.session() as session:
            session.run("""
            MERGE (e:Entity {name: $name, type: $type})
            """, name=entity_name, type=entity_type)

    def create_relationship(self, source, target, relationship):
        with self.driver.session() as session:
            session.run("""
            MATCH (a:Entity {name: $source}), (b:Entity {name: $target})
            MERGE (a)-[:RELATES_TO {type: $relationship}]->(b)
            """, source=source, target=target, relationship=relationship)

    
# Step 2: Define PDF Processor
def extract_text_from_pdfs(pdf_paths):
    
    texts = []
    for pdf_path in pdf_paths:
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        texts.append(" ".join([doc.page_content for doc in documents]))
    return texts

# Step 3: Entity Extraction with spaCy
nlp = spacy.load("en_core_web_sm")

def extract_entities_and_relationships(text):
    
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    relationships = []  # Example placeholder, can be expanded with logic to detect relationships.
    
    # Here we simply associate some basic relationships based on entities (can be extended)
    for i in range(len(entities)-1):
        relationships.append((entities[i][0], "RELATED_TO", entities[i+1][0]))

    return entities, relationships

# Step 4: Process Knowledge Graph Data
def process_knowledge_graph_data(entities, relationships, neo4j_kg):
    
    for entity, entity_type in entities:
        neo4j_kg.create_entity(entity, entity_type)
        
    for source, rel, target in relationships:
        neo4j_kg.create_relationship(source, target, rel)


