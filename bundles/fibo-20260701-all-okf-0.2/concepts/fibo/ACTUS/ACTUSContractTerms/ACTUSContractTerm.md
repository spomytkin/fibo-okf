---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract term
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: code denoting a term describing an aspect of one or more ACTUS contract type(s)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#string
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/hasParameterName
  - filler: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/characterizes
  - filler: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Collections/isMemberOf
    value: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/AlgorithmicContractTypesDataDictionary
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasTag
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/hasTextualName
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/AlgorithmicContractTypesDataDictionary
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS contract term
type: Ontology Class
---

# ACTUS contract term

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm>

## Definition

code denoting a term describing an aspect of one or more ACTUS contract type(s)

## Relationships

- **Subclass of**: [CodeElement](<https://www.omg.org/spec/Commons/CodesAndCodeSets/CodeElement>)

## Constraints

- **[hasParameterName](/concepts/fibo/ACTUS/ACTUSContractTerms/hasParameterName.md)**: exact qualified cardinality 1 of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[characterizes](<https://www.omg.org/spec/Commons/Classifiers/characterizes>)**: some values from of type [ACTUSContractType](/concepts/fibo/ACTUS/ACTUSTaxonomy/ACTUSContractType.md)
- **[isClassifiedBy](<https://www.omg.org/spec/Commons/Classifiers/isClassifiedBy>)**: some values from of type [ACTUSContractTermGroup](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup.md)
- **[isMemberOf](<https://www.omg.org/spec/Commons/Collections/isMemberOf>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/AlgorithmicContractTypesDataDictionary`
- **[hasTag](<https://www.omg.org/spec/Commons/Designators/hasTag>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[hasTextualName](<https://www.omg.org/spec/Commons/Designators/hasTextualName>)**: some values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/AlgorithmicContractTypesDataDictionary`

## Annotations

- **label**: ACTUS contract term
- **definition**: code denoting a term describing an aspect of one or more ACTUS contract type(s)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
