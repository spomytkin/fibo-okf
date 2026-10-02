---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS dictionary term group
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for a collection of ACTUS dictionary parameters that tend to be applied together
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTerm
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/AlgorithmicContractTypesDataDictionary
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup
sources:
- id: fibo-source-693c1adb8c
  resource: references/fibo/ACTUS/ACTUSContractTerms.rdf
  sha256: 693c1adb8cb72d5497fad9bf041c21f2b8c3852f8267b04a354a42a7ee38f986
  title: FIBO source ACTUS/ACTUSContractTerms.rdf
title: ACTUS dictionary term group
type: Ontology Class
---

# ACTUS dictionary term group

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/ACTUSContractTermGroup>

## Definition

classifier for a collection of ACTUS dictionary parameters that tend to be applied together

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [ACTUSContractTerm](/concepts/fibo/ACTUS/ACTUSContractTerms/ACTUSContractTerm.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSContractTerms/AlgorithmicContractTypesDataDictionary`

## Annotations

- **label**: ACTUS dictionary term group
- **definition**: classifier for a collection of ACTUS dictionary parameters that tend to be applied together

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
