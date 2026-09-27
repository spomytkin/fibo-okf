---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CT - LAX
  - datatype: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
    value: '4'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: exoticLinearAmortizer
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: Lending agreements with exotic repayment schedules.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: LAX
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Exotic Linear Amortizer
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/ACTUSContractType-ExoticLinearAmortizer.md
    predicate: https://www.omg.org/spec/Commons/Designators/denotes
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-ExoticLinearAmortizer
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT-LAX
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CT - LAX
type: Ontology Individual
---

# ACTUS contract term - CT - LAX

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT-LAX>

## Relationships

- **Related to**: [ACTUSContractTerm-CT](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT.md)
- **Related to**: [ACTUSContractType-ExoticLinearAmortizer](/concepts/fibo/ACTUS/ACTUSTaxonomy/ACTUSContractType-ExoticLinearAmortizer.md)

## Annotations

- **label**: ACTUS contract term - CT - LAX
- **hasOptionSequenceNumber**: 4
- **hasParameterName**: exoticLinearAmortizer
- **hasDescription**: Lending agreements with exotic repayment schedules.
- **hasTag**: LAX
- **hasTextualName**: Exotic Linear Amortizer

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
