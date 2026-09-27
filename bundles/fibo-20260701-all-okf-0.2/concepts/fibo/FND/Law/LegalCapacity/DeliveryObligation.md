---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: delivery obligation
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: obligation to deliver something in order to satisfy a claim or debt
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A delivery obligation is the responsibility of one party to deliver goods, services, instruments, money, or other
      specified items to another party, typically as outlined in an agreement. Failure to do so may result in breach of contract
      if the obligation is specified as such, which may have further legal ramifications.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Law/LegalCapacity/ContingentObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/ContingentObligation
  - concept: /concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/LegalObligation
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/DeliveryObligation
sources:
- id: fibo-source-544b6eb4c7
  resource: references/fibo/FND/Law/LegalCapacity.rdf
  sha256: 544b6eb4c7d0acd6efdeb794a9af17ec89bec5145b178192396defaa50bbef22
  title: FIBO source FND/Law/LegalCapacity.rdf
title: delivery obligation
type: Ontology Class
---

# delivery obligation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Law/LegalCapacity/DeliveryObligation>

## Definition

obligation to deliver something in order to satisfy a claim or debt

## Relationships

- **Subclass of**: [ContingentObligation](/concepts/fibo/FND/Law/LegalCapacity/ContingentObligation.md)
- **Subclass of**: [LegalObligation](/concepts/fibo/FND/Law/LegalCapacity/LegalObligation.md)

## Annotations

- **label** (en): delivery obligation
- **definition** (en): obligation to deliver something in order to satisfy a claim or debt
- **explanatoryNote** (en): A delivery obligation is the responsibility of one party to deliver goods, services, instruments, money, or other specified items to another party, typically as outlined in an agreement. Failure to do so may result in breach of contract if the obligation is specified as such, which may have further legal ramifications.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
