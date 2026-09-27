---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CT - UMP
  - datatype: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
    value: '6'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: undefinedMaturityProfile
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Interest paying cash accounts (current / savings / etc.).
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: UMP
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Undefined Maturity Profile
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/ACTUSContractType-UndefinedMaturityProfile.md
    predicate: https://www.omg.org/spec/Commons/Designators/denotes
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-UndefinedMaturityProfile
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT-UMP
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CT - UMP
type: Ontology Individual
---

# ACTUS contract term - CT - UMP

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT-UMP>

## Relationships

- **Related to**: [ACTUSContractTerm-CT](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT.md)
- **Related to**: [ACTUSContractType-UndefinedMaturityProfile](/concepts/fibo/ACTUS/ACTUSTaxonomy/ACTUSContractType-UndefinedMaturityProfile.md)

## Annotations

- **label**: ACTUS contract term - CT - UMP
- **hasOptionSequenceNumber**: 6
- **hasParameterName**: undefinedMaturityProfile
- **hasDescription**: Interest paying cash accounts (current / savings / etc.).
- **hasTag**: UMP
- **hasTextualName**: Undefined Maturity Profile

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
