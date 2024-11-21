# Step 5: Main Project Workflow
def main():
    # Neo4j configuration
    neo4j_uri = "bolt://localhost:7687"
    neo4j_username = "neo4j"
    neo4j_password = "Test1234"

    # Initialize Neo4j Knowledge Graph
    neo4j_kg = Neo4jKnowledgeGraph(neo4j_uri, neo4j_username, neo4j_password)

    # Define PDF files
    initial_pdfs = [f"document{i+1}.pdf" for i in range(5)]  # First 5 PDFs
    additional_pdfs = [f"document{i+6}.pdf" for i in range(5)]  # Next 5 PDFs

    # Extract text from PDFs
    all_texts = extract_text_from_pdfs(initial_pdfs + additional_pdfs)

    # Process initial PDFs (After 5 PDFs)
    print("Processing initial 5 PDFs...")
    for text in all_texts[:5]:
        entities, relationships = extract_entities_and_relationships(text)
        process_knowledge_graph_data(entities, relationships, neo4j_kg)

    
    # Evolve with additional PDFs (After 10 PDFs)
    print("\nProcessing additional 5 PDFs...")
    for text in all_texts[5:]:
        entities, relationships = extract_entities_and_relationships(text)
        process_knowledge_graph_data(entities, relationships, neo4j_kg)

    # Clean up
    neo4j_kg.close()
    print("Knowledge Graph Updated Successfully!")

if __name__ == "__main__":
    main()