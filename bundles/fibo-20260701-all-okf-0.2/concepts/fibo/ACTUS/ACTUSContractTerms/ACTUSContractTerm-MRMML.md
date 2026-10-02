---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - MRMML
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: maintenanceMarginLowerBound
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Defines the lower bound of the Maintenance Margin. If MRVM falls below MRMML, then capital must be added to reach
      the original MRIM.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: MRMML
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Maintenance Margin Lower Bound
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Margining.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Margining
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-MRMML
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - MRMML
type: Ontology Individual
---

# ACTUS contract term - MRMML

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-MRMML>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Margining](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Margining.md)

## Annotations

- **label**: ACTUS contract term - MRMML
- **hasParameterName**: maintenanceMarginLowerBound
- **hasDescription**: Defines the lower bound of the Maintenance Margin. If MRVM falls below MRMML, then capital must be added to reach the original MRIM.
- **hasTag**: MRMML
- **hasTextualName**: Maintenance Margin Lower Bound

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
