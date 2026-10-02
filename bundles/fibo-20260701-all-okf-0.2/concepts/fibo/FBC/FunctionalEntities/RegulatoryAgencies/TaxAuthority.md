---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tax authority
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: regulatory agency that has jurisdiction over the assessment, determination, collection, imposition and other aspects
      of any tax
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.collinsdictionary.com/dictionary/english/tax-authority
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.lawinsider.com/dictionary/tax-authority
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentifier
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/issues
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentificationScheme
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Organizations/manages
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/TaxAuthority
sources:
- id: fibo-source-ef717d20cc
  resource: references/fibo/FBC/FunctionalEntities/RegulatoryAgencies.rdf
  sha256: ef717d20cc3804b8cc9643a625bf716211db11cc374a524b54dd5ce7e70bf1db
  title: FIBO source FBC/FunctionalEntities/RegulatoryAgencies.rdf
title: tax authority
type: Ontology Class
---

# tax authority

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/RegulatoryAgencies/TaxAuthority>

## Definition

regulatory agency that has jurisdiction over the assessment, determination, collection, imposition and other aspects of any tax

## Relationships

- **Subclass of**: [RegulatoryAgency](<https://www.omg.org/spec/Commons/RegulatoryAgencies/RegulatoryAgency>)

## Constraints

- **[issues](/concepts/fibo/FND/Relations/Relations/issues.md)**: min qualified cardinality 0 of type [TaxIdentifier](/concepts/fibo/FND/Parties/Parties/TaxIdentifier.md)
- **[manages](<https://www.omg.org/spec/Commons/Organizations/manages>)**: some values from of type [TaxIdentificationScheme](/concepts/fibo/FND/Parties/Parties/TaxIdentificationScheme.md)
- **[hasJurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/hasJurisdiction>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: tax authority
- **definition**: regulatory agency that has jurisdiction over the assessment, determination, collection, imposition and other aspects of any tax
- **adaptedFrom**: https://www.collinsdictionary.com/dictionary/english/tax-authority
- **adaptedFrom**: https://www.lawinsider.com/dictionary/tax-authority

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
