---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: consumer credit equal treatment requirement
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/EqualTreatmentRight
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/confers
  subclass_of:
  - concept: /concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditRequirement.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditRequirement
resource: https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditEqualTreatmentRequirement
sources:
- id: fibo-source-9d1d4cf0d4
  resource: references/fibo/LOAN/LoansGeneral/LoansRegulatory.rdf
  sha256: 9d1d4cf0d45e2966f6fbe27dd62486cdd11c427c2d40f7701ea8f1775769245b
  title: FIBO source LOAN/LoansGeneral/LoansRegulatory.rdf
title: consumer credit equal treatment requirement
type: Ontology Class
---

# consumer credit equal treatment requirement

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditEqualTreatmentRequirement>

## Relationships

- **Subclass of**: [ConsumerCreditRequirement](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/ConsumerCreditRequirement.md)

## Constraints

- **[confers](/concepts/fibo/FND/Relations/Relations/confers.md)**: some values from of type [EqualTreatmentRight](/concepts/fibo/LOAN/LoansGeneral/LoansRegulatory/EqualTreatmentRight.md)

## Annotations

- **label** (en): consumer credit equal treatment requirement

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
