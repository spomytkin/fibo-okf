---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term - CTS
  - predicate: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
    value: contractStructure
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: This should really map to a collection of contracts or a single contract, but to map it properly requires input
      from the ACTUS experts. Depends on what ACTUS means by contract structure.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasDescription
    value: A structure identifying individual or sets of underlying contracts. E.g. for FUTUR, this structure identifies the
      single underlying contract, for SWAPS, the FirstLeg and SecondLeg are identified, or for CEG, CEC the structure identifies
      Covered and Covering contracts.
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTag
    value: CTS
  - predicate: https://www.omg.org/spec/Commons/Designators/hasTextualName
    value: Contract Structure
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
  related_to:
  - concept: /concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md
    predicate: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CTS
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term - CTS
type: Ontology Individual
---

# ACTUS contract term - CTS

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm-CTS>

## Relationships

- **Related to**: [ACTUSContractTermGroup-ContractIdentification](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup-ContractIdentification.md)

## Annotations

- **label**: ACTUS contract term - CTS
- **hasParameterName**: contractStructure
- **explanatoryNote**: This should really map to a collection of contracts or a single contract, but to map it properly requires input from the ACTUS experts. Depends on what ACTUS means by contract structure.
- **hasDescription**: A structure identifying individual or sets of underlying contracts. E.g. for FUTUR, this structure identifies the single underlying contract, for SWAPS, the FirstLeg and SecondLeg are identified, or for CEG, CEC the structure identifies Covered and Covering contracts.
- **hasTag**: CTS
- **hasTextualName**: Contract Structure

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
