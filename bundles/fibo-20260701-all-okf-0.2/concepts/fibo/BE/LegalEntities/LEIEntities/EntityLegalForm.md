---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: entity legal form
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a classifier for a legal entity that indicates the nature of that entity as defined from a legal or regulatory
      perspective, in the jurisdiction in which it was established
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso.org/obp/ui/#iso:std:iso:20275:ed-1:v1:en
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/TextDatatype/Text
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/TextDatatype/Text
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasTransliteratedLegalFormAbbreviation
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/TextDatatype/Text
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/hasTransliteratedName
  - filler: https://www.omg.org/spec/Commons/Organizations/LegalPerson
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/TextDatatype/Text
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/hasTextualName
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalFormScheme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Classifier
resource: https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalForm
sources:
- id: fibo-source-535adad55c
  resource: references/fibo/BE/LegalEntities/LEIEntities.rdf
  sha256: 535adad55c4f6fe3ad7131256c4a1602e8c4727fbef1a89c338de8d9559a4cca
  title: FIBO source BE/LegalEntities/LEIEntities.rdf
title: entity legal form
type: Ontology Class
---

# entity legal form

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/LegalEntities/LEIEntities/EntityLegalForm>

## Definition

a classifier for a legal entity that indicates the nature of that entity as defined from a legal or regulatory perspective, in the jurisdiction in which it was established

## Relationships

- **Subclass of**: [Classifier](<https://www.omg.org/spec/Commons/Classifiers/Classifier>)

## Constraints

- **[hasLegalFormAbbreviation](/concepts/fibo/BE/LegalEntities/LEIEntities/hasLegalFormAbbreviation.md)**: min qualified cardinality 0 of type [Text](<https://www.omg.org/spec/Commons/TextDatatype/Text>)
- **[hasTransliteratedLegalFormAbbreviation](/concepts/fibo/BE/LegalEntities/LEIEntities/hasTransliteratedLegalFormAbbreviation.md)**: min qualified cardinality 0 of type [Text](<https://www.omg.org/spec/Commons/TextDatatype/Text>)
- **[hasTransliteratedName](/concepts/fibo/BE/LegalEntities/LEIEntities/hasTransliteratedName.md)**: min qualified cardinality 0 of type [Text](<https://www.omg.org/spec/Commons/TextDatatype/Text>)
- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [LegalPerson](<https://www.omg.org/spec/Commons/Organizations/LegalPerson>)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)
- **[hasTextualName](<https://www.omg.org/spec/Commons/Designators/hasTextualName>)**: min qualified cardinality 0 of type [Text](<https://www.omg.org/spec/Commons/TextDatatype/Text>)
- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: some values from of type [EntityLegalFormScheme](/concepts/fibo/BE/LegalEntities/LEIEntities/EntityLegalFormScheme.md)

## Annotations

- **label**: entity legal form
- **definition**: a classifier for a legal entity that indicates the nature of that entity as defined from a legal or regulatory perspective, in the jurisdiction in which it was established
- **adaptedFrom**: https://www.gleif.org/en/about-lei/common-data-file-format/lei-cdf-format/lei-cdf-format-version-2-1
- **adaptedFrom**: https://www.iso.org/obp/ui/#iso:std:iso:20275:ed-1:v1:en

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
