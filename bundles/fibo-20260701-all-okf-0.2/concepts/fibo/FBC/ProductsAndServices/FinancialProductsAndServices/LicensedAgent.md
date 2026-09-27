---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: licensed agent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any individual who is licensed to perform a legally binding function, and who has been legally empowered to act
      on behalf of another party
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Insurance agents, realtors, financial advisors, certain attorneys, and brokers are examples of legal agents.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 17 CFR 45.1, Definitions - see the definition of agent
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent
  - concept: /concepts/fibo/FND/Law/LegalCapacity/Licensee.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/Licensee
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/LicensedAgent
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: licensed agent
type: Ontology Class
---

# licensed agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/LicensedAgent>

## Definition

any individual who is licensed to perform a legally binding function, and who has been legally empowered to act on behalf of another party

## Relationships

- **Subclass of**: [LegalAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md)
- **Subclass of**: [Licensee](/concepts/fibo/FND/Law/LegalCapacity/Licensee.md)
- **Subclass of**: [ResponsibleParty](<https://www.omg.org/spec/Commons/BusinessAuthorizations/ResponsibleParty>)

## Annotations

- **label**: licensed agent
- **definition**: any individual who is licensed to perform a legally binding function, and who has been legally empowered to act on behalf of another party
- **example**: Insurance agents, realtors, financial advisors, certain attorneys, and brokers are examples of legal agents.
- **adaptedFrom**: 17 CFR 45.1, Definitions - see the definition of agent

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
