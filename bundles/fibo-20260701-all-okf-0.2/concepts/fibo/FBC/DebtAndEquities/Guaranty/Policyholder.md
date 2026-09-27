---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: policyholder
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: counterparty to and typically owner of an insurance policy
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: insured party
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/Counterparty.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/Counterparty
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Policyholder
sources:
- id: fibo-source-a6bc9592ee
  resource: references/fibo/FBC/DebtAndEquities/Guaranty.rdf
  sha256: a6bc9592eeebb061e99b2dc168751d4b3612dbcc32c86c50959e17011e4247b0
  title: FIBO source FBC/DebtAndEquities/Guaranty.rdf
title: policyholder
type: Ontology Class
---

# policyholder

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Guaranty/Policyholder>

## Definition

counterparty to and typically owner of an insurance policy

## Relationships

- **Subclass of**: [Counterparty](/concepts/fibo/FND/Agreements/Contracts/Counterparty.md)

## Annotations

- **label**: policyholder
- **definition**: counterparty to and typically owner of an insurance policy
- **synonym**: insured party

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
