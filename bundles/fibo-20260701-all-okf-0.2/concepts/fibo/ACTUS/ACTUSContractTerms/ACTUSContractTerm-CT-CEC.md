---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CT - CEC
  - datatype: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
    value: '17'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: creditEnhancementCollateral
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: A collateral securing the scheduled payment obligations of an underlying instrument
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: CEC
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Credit Enhancement Collateral
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/ACTUSContractType-Collateral.md
    predicate: https://www.omg.org/spec/Commons/Designators/denotes
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-Collateral
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT-CEC
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CT - CEC
type: Ontology Individual
---

# ACTUS contract term - CT - CEC

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT-CEC>

## Relationships

- **Related to**: [ACTUSContractTerm-CT](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT.md)
- **Related to**: [ACTUSContractType-Collateral](/concepts/fibo/ACTUS/ACTUSTaxonomy/ACTUSContractType-Collateral.md)

## Annotations

- **label**: ACTUS contract term - CT - CEC
- **hasOptionSequenceNumber**: 17
- **hasParameterName**: creditEnhancementCollateral
- **hasDescription**: A collateral securing the scheduled payment obligations of an underlying instrument
- **hasTag**: CEC
- **hasTextualName**: Credit Enhancement Collateral

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
