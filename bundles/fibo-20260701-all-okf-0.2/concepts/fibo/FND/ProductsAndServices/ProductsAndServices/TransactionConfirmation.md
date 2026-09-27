---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: transaction confirmation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: written communication from a seller or service provider reciting the relevant details of a transaction
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionEvent
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidenceFor
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Documents/LegalDocument
resource: https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation
sources:
- id: fibo-source-7f330c2b6d
  resource: references/fibo/FND/ProductsAndServices/ProductsAndServices.rdf
  sha256: 7f330c2b6de4e90f2c5d728ddf32af1d75f320646040450c1da9a8c5f8740548
  title: FIBO source FND/ProductsAndServices/ProductsAndServices.rdf
title: transaction confirmation
type: Ontology Class
---

# transaction confirmation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/ProductsAndServices/ProductsAndServices/TransactionConfirmation>

## Definition

written communication from a seller or service provider reciting the relevant details of a transaction

## Relationships

- **Subclass of**: [LegalDocument](<https://www.omg.org/spec/Commons/Documents/LegalDocument>)

## Constraints

- **[isEvidenceFor](/concepts/fibo/FND/Agreements/Contracts/isEvidenceFor.md)**: exact qualified cardinality 1 of type [TransactionEvent](/concepts/fibo/FND/ProductsAndServices/ProductsAndServices/TransactionEvent.md)

## Annotations

- **label**: transaction confirmation
- **definition**: written communication from a seller or service provider reciting the relevant details of a transaction

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
