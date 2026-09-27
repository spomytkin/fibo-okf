---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: dealer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: any party that purchases goods or services for resale and acts on their own behalf in a transaction
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A dealer is a counterparty or principal in the transaction with the customer.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/ServiceProvider
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Dealer
sources:
- id: fibo-source-4fc675338a
  resource: references/fibo/FBC/ProductsAndServices/FinancialProductsAndServices.rdf
  sha256: 4fc675338a28c5419555e56e545b4aa6b0686d14777b4b852624b166d585b5ca
  title: FIBO source FBC/ProductsAndServices/FinancialProductsAndServices.rdf
title: dealer
type: Ontology Class
---

# dealer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/ProductsAndServices/FinancialProductsAndServices/Dealer>

## Definition

any party that purchases goods or services for resale and acts on their own behalf in a transaction

## Relationships

- **Subclass of**: [ServiceProvider](<https://www.omg.org/spec/Commons/Organizations/ServiceProvider>)

## Annotations

- **label**: dealer
- **definition**: any party that purchases goods or services for resale and acts on their own behalf in a transaction
- **explanatoryNote**: A dealer is a counterparty or principal in the transaction with the customer.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
