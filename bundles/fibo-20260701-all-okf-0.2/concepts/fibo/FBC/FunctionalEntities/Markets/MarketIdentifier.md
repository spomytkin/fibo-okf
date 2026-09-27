---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: identifier that specifies a universal method of identifying exchanges, trading platforms, regulated or non-regulated
      markets, and data reporting services providers as sources of prices and related information in order to facilitate automated
      processing
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: MIC
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10383, Securities and related financial instruments - Codes for exchanges and market identification (MIC),
      Third edition, 2012-10-01
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/market-identifier-codes
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'It is intended for use in any application and communication for identification of places

      - where a financial instrument is listed (place of official listing),

      - where a related trade is executed (place of trade), and

      - where trade details are reported (trade reporting facility).'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: Market Identifier Code
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
    value: Nb76d3df2997b4688b49ec482d8a88e1e
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Identifiers/Identifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifier
sources:
- id: fibo-source-c024989361
  resource: references/fibo/FBC/FunctionalEntities/Markets.rdf
  sha256: c0249893617f6c64fb6b454763bcddfb73748067a0ae183e40b432e03fde24bf
  title: FIBO source FBC/FunctionalEntities/Markets.rdf
title: market identifier
type: Ontology Class
---

# market identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/MarketIdentifier>

## Definition

identifier that specifies a universal method of identifying exchanges, trading platforms, regulated or non-regulated markets, and data reporting services providers as sources of prices and related information in order to facilitate automated processing

## Relationships

- **Subclass of**: [Identifier](<https://www.omg.org/spec/Commons/Identifiers/Identifier>)

## Constraints

- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: some values from value `Nb76d3df2997b4688b49ec482d8a88e1e`

## Annotations

- **label**: market identifier
- **definition**: identifier that specifies a universal method of identifying exchanges, trading platforms, regulated or non-regulated markets, and data reporting services providers as sources of prices and related information in order to facilitate automated processing
- **abbreviation**: MIC
- **adaptedFrom**: ISO 10383, Securities and related financial instruments - Codes for exchanges and market identification (MIC), Third edition, 2012-10-01
- **adaptedFrom**: https://www.iso20022.org/market-identifier-codes
- **adaptedFrom**: https://www.iso20022.org/sites/default/files/2021-12/ISO10383_MIC_Release_2_0_Factsheet.pdf
- **explanatoryNote**: It is intended for use in any application and communication for identification of places - where a financial instrument is listed (place of official listing), - where a related trade is executed (place of trade), and - where trade details are reported (trade reporting facility).
- **synonym**: Market Identifier Code

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
