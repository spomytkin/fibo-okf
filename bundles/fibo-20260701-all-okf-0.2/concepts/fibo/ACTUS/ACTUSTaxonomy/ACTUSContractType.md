---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ACTUS contract type
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: classifier for an algorithmic capability, i.e., the rules, from which the cashflows for a credit agreement, financial
      instrument or related contract, based on their characteristics, can be analyzed
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Cashflows in ACTUS are classified as basic, combined / derivatives, or credit enhancement, and then each of these
      areas breaks down into a number of subclassifications.
  - predicate: https://www.omg.org/spec/Commons/TextDatatype/hasTextValue
    value: CT
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: http://www.w3.org/2001/XMLSchema#string
    kind: all_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/hasCoverageDescription
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CashFlows/CashFlowStructure
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - kind: has_value
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
    value: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/refersTo
    value: N669a2a3bb899499da6428c958ed52a96
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType
sources:
- id: fibo-source-1ffe76217e
  resource: references/fibo/ACTUS/ACTUSContractTermMapping.rdf
  sha256: 1ffe76217e0123653c8a4d03290dcfab352af9fe7a5cdb369ae0e86c55d11bbd
  title: FIBO source ACTUS/ACTUSContractTermMapping.rdf
- id: fibo-source-c715cd4f2e
  resource: references/fibo/ACTUS/ACTUSTaxonomy.rdf
  sha256: c715cd4f2e23f8986a6965786f676ee8eeea6c0496f96a0dd57306fe5907a24a
  title: FIBO source ACTUS/ACTUSTaxonomy.rdf
title: ACTUS contract type
type: Ontology Class
---

# ACTUS contract type

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/ACTUSContractType>

## Definition

classifier for an algorithmic capability, i.e., the rules, from which the cashflows for a credit agreement, financial instrument or related contract, based on their characteristics, can be analyzed

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[hasCoverageDescription](/concepts/fibo/ACTUS/ACTUSTaxonomy/hasCoverageDescription.md)**: all values from of type [string](<http://www.w3.org/2001/XMLSchema#string>)
- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [CashFlowStructure](/concepts/fibo/FND/Accounting/CashFlows/CashFlowStructure.md)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: has value value `https://spec.edmcouncil.org/fibo/ontology/ACTUS/ACTUSTaxonomy/AlgorithmicContractTypesClassificationScheme`
- **[refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)**: some values from value `N669a2a3bb899499da6428c958ed52a96`

## Annotations

- **label**: ACTUS contract type
- **definition**: classifier for an algorithmic capability, i.e., the rules, from which the cashflows for a credit agreement, financial instrument or related contract, based on their characteristics, can be analyzed
- **explanatoryNote**: Cashflows in ACTUS are classified as basic, combined / derivatives, or credit enhancement, and then each of these areas breaks down into a number of subclassifications.
- **hasTextValue**: CT

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
