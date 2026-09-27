---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: third-party agent
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any service provider that is licensed to perform a legally binding function and has been legally empowered to act
      on behalf of another party
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 17 CFR 45.1, Definitions - see the definition of agent
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/usageNote
    value: Note that third-party agent is defined as a service provider (organization) acting in an agency capacity, such
      as a law firm, accountancy, or investment bank. This is distinct from the concept of an individual (licensed agent),
      for example one who works for a broker-dealer, that is a registered agent licensed to sell securities.
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
    resource: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: third-party agent
type: Ontology Class
---

# third-party agent

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/ThirdPartyAgent>

## Definition

any service provider that is licensed to perform a legally binding function and has been legally empowered to act on behalf of another party

## Relationships

- **Subclass of**: [LegalAgent](/concepts/fibo/FBC/ProductsAndServices/FinancialProductsAndServices/LegalAgent.md)
- **Subclass of**: [Licensee](/concepts/fibo/FND/Law/LegalCapacity/Licensee.md)
- **Subclass of**: [ServiceProvider](<https://www.omg.org/spec/Commons/Organizations/ServiceProvider>)

## Annotations

- **label**: third-party agent
- **definition**: any service provider that is licensed to perform a legally binding function and has been legally empowered to act on behalf of another party
- **adaptedFrom**: 17 CFR 45.1, Definitions - see the definition of agent
- **usageNote**: Note that third-party agent is defined as a service provider (organization) acting in an agency capacity, such as a law firm, accountancy, or investment bank. This is distinct from the concept of an individual (licensed agent), for example one who works for a broker-dealer, that is a registered agent licensed to sell securities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
