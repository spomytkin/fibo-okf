---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - BEF
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: boundaryEffect
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: This term specifies which leg - if any- becomes the active subcontract when the underlying asset's price crosses
      the specified boundary value in the specified direction triggerring a boundary crossing event.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: BEF
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Boundary Effect
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Boundary.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Boundary
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-BEF
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - BEF
type: Ontology Individual
---

# ACTUS contract term - BEF

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-BEF>

## Relationships

- **Related to**: [ACTUSContractTermGroup-Boundary](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-Boundary.md)

## Annotations

- **label**: ACTUS contract term - BEF
- **hasParameterName**: boundaryEffect
- **hasDescription**: This term specifies which leg - if any- becomes the active subcontract when the underlying asset's price crosses the specified boundary value in the specified direction triggerring a boundary crossing event.
- **hasTag**: BEF
- **hasTextualName**: Boundary Effect

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
