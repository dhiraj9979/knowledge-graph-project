This project demonstrates how to create and visualize a knowledge graph by processing textual data from PDF documents. 
The knowledge graph is stored in a Neo4j database and evolves dynamically as new data is ingested. 
The system adheres to software engineering best practices, ensuring a scalable, maintainable, and robust implementation.

Features

    Dynamic Knowledge Graph Construction:
        Ingests batches of PDFs to extract meaningful relationships.
        Constructs and updates a Neo4j knowledge graph.
    Batch Processing:
        Processes 5 PDFs initially, with additional PDFs added incrementally.
        Ensures the graph evolves without redundant reprocessing.
    Visualization:
        Visualizes the graph in Neo4j's UI.
    Error Handling:
        Robust error management during PDF ingestion, graph updates, and database interactions.
    Scalability:
        Designed for seamless integration with larger datasets and workflows.
