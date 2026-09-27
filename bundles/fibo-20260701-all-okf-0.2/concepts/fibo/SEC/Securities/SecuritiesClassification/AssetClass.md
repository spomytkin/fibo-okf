---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: asset class
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: financial instrument classifier for a group of securities that exhibit similar characteristics, behave similarly
      in the marketplace and are subject to the same laws and regulations
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.investopedia.com/terms/a/assetclasses.asp
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.law.cornell.edu/cfr/text/17/45.1
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Asset class means the broad category of goods, services or commodities, including any 'excluded commodity' as defined
      in CEA section 1a(19), with common characteristics underlying a swap. The asset classes include credit, equity, foreign
      exchange (excluding cross-currency), interest rate (including cross-currency), other commodity, and such other asset
      classes as may be determined by the Commission.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The three main asset classes are equities, or stocks; fixed income, or bonds; and cash equivalents, or money market
      instruments. Some investment professionals add real estate and commodities, and possibly other types of investments,
      to the asset class mix.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/AssetClass
sources:
- id: fibo-source-6fed3fa3dd
  resource: references/fibo/SEC/Securities/SecuritiesClassification.rdf
  sha256: 6fed3fa3ddd850e875bf020fa5eb79e1d90023fb74888e9c1856e32882bc8f76
  title: FIBO source SEC/Securities/SecuritiesClassification.rdf
title: asset class
type: Ontology Class
---

# asset class

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/AssetClass>

## Definition

financial instrument classifier for a group of securities that exhibit similar characteristics, behave similarly in the marketplace and are subject to the same laws and regulations

## Relationships

- **Subclass of**: [FinancialInstrumentClassifier](/concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Annotations

- **label**: asset class
- **definition**: financial instrument classifier for a group of securities that exhibit similar characteristics, behave similarly in the marketplace and are subject to the same laws and regulations
- **adaptedFrom**: http://www.investopedia.com/terms/a/assetclasses.asp
- **adaptedFrom**: https://www.law.cornell.edu/cfr/text/17/45.1
- **explanatoryNote**: Asset class means the broad category of goods, services or commodities, including any 'excluded commodity' as defined in CEA section 1a(19), with common characteristics underlying a swap. The asset classes include credit, equity, foreign exchange (excluding cross-currency), interest rate (including cross-currency), other commodity, and such other asset classes as may be determined by the Commission.
- **explanatoryNote**: The three main asset classes are equities, or stocks; fixed income, or bonds; and cash equivalents, or money market instruments. Some investment professionals add real estate and commodities, and possibly other types of investments, to the asset class mix.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
