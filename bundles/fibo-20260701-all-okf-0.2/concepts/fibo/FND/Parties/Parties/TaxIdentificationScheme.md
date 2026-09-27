---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tax identification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identification scheme used to identify taxpayers in some jurisdiction
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.oecd-ilibrary.org/taxation/standard-for-automatic-exchange-of-financial-account-information-in-tax-matters-second-edition_9789264267992-en
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentificationScheme
sources:
- id: fibo-source-2c7ef9cc41
  resource: references/fibo/FND/Parties/Parties.rdf
  sha256: 2c7ef9cc4107e85b5bba3894094e496bcf4e8fe3ef9d6ce3b7d0830fb284f61d
  title: FIBO source FND/Parties/Parties.rdf
title: tax identification scheme
type: Ontology Class
---

# tax identification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/TaxIdentificationScheme>

## Definition

identification scheme used to identify taxpayers in some jurisdiction

## Relationships

- **Subclass of**: [IdentificationScheme](<https://www.omg.org/spec/Commons/Identifiers/IdentificationScheme>)

## Constraints

- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: some values from of type [Jurisdiction](<https://www.omg.org/spec/Commons/RegulatoryAgencies/Jurisdiction>)

## Annotations

- **label**: tax identification scheme
- **definition**: identification scheme used to identify taxpayers in some jurisdiction
- **adaptedFrom**: https://www.oecd-ilibrary.org/taxation/standard-for-automatic-exchange-of-financial-account-information-in-tax-matters-second-edition_9789264267992-en

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
