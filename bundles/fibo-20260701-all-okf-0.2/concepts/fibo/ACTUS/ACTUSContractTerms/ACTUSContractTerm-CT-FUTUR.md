---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CT - FUTUR
  - datatype: http://www.w3.org/2001/XMLSchema#nonNegativeInteger
    predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasOptionSequenceNumber
    value: '14'
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: future
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: An agreement of exchanging an underlying instrument against a fixed price in the future.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: FUTUR
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Future
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT.md
    predicate: https://www.omg.org/spec/Commons/Collections/isMemberOf
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT
  - concept: /concepts/fibo/ACTUS/ACTUSTaxonomy/ACTUSContractType-Future.md
    predicate: https://www.omg.org/spec/Commons/Designators/denotes
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType-Future
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT-FUTUR
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CT - FUTUR
type: Ontology Individual
---

# ACTUS contract term - CT - FUTUR

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT-FUTUR>

## Relationships

- **Related to**: [ACTUSContractTerm-CT](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CT.md)
- **Related to**: [ACTUSContractType-Future](/concepts/fibo/ACTUS/ACTUSTaxonomy/ACTUSContractType-Future.md)

## Annotations

- **label**: ACTUS contract term - CT - FUTUR
- **hasOptionSequenceNumber**: 14
- **hasParameterName**: future
- **hasDescription**: An agreement of exchanging an underlying instrument against a fixed price in the future.
- **hasTag**: FUTUR
- **hasTextualName**: Future

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
