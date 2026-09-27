---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Basel III Designation
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: European Union wide securities designation, defined by the Basel Committee on Banking Supervision (BCBS), that
      classifies securities based on the quality of capital underlying the instrument
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bis.org/bcbs/basel3.htm
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.bis.org/bcbs/index.htm
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Basel III is an international regulatory accord designed to improve the regulation, supervision, and risk management
      of the banking sector. It was developed in response to the global financial crisis of 2007-2008. A consortium of central
      banks from 28 countries devised Basel III in 2009, mainly to ensure major banks could survive another upheaval. The
      regulations include minimum capital, leverage, and liquidity requirements.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Per Basel III, Tier 1 capital, or core capital, equity shares and retained earnings, is preferred. Tier 2 capital,
      or supplementary capital, is also usable. Possible values include Tier 1, Additional Tier 1, Tier 2, Not Subject to
      Regulations, and Not Provided.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Classifiers/classifies
  - kind: has_value
    property: https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn
    value: https://www.omg.org/spec/Commons/Locations/GeographicRegion
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/BaselIIIDesignation
sources:
- id: fibo-source-d2c4e0b02d
  resource: references/fibo/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.rdf
  sha256: d2c4e0b02d30114692ca293e6f51e26b36eef9f530171ac73c4831c6e7869087
  title: FIBO source SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.rdf
title: Basel III Designation
type: Ontology Class
---

# Basel III Designation

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/BaselIIIDesignation>

## Definition

European Union wide securities designation, defined by the Basel Committee on Banking Supervision (BCBS), that classifies securities based on the quality of capital underlying the instrument

## Relationships

- **Subclass of**: [FinancialInstrumentClassifier](/concepts/fibo/SEC/Securities/SecuritiesClassification/FinancialInstrumentClassifier.md)

## Constraints

- **[classifies](<https://www.omg.org/spec/Commons/Classifiers/classifies>)**: some values from of type [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **[isApplicableIn](<https://www.omg.org/spec/Commons/ContextualDesignators/isApplicableIn>)**: has value value `https://www.omg.org/spec/Commons/Locations/GeographicRegion`

## Annotations

- **label**: Basel III Designation
- **definition**: European Union wide securities designation, defined by the Basel Committee on Banking Supervision (BCBS), that classifies securities based on the quality of capital underlying the instrument
- **adaptedFrom**: https://www.bis.org/bcbs/basel3.htm
- **adaptedFrom**: https://www.bis.org/bcbs/index.htm
- **explanatoryNote**: Basel III is an international regulatory accord designed to improve the regulation, supervision, and risk management of the banking sector. It was developed in response to the global financial crisis of 2007-2008. A consortium of central banks from 28 countries devised Basel III in 2009, mainly to ensure major banks could survive another upheaval. The regulations include minimum capital, leverage, and liquidity requirements.
- **explanatoryNote**: Per Basel III, Tier 1 capital, or core capital, equity shares and retained earnings, is preferred. Tier 2 capital, or supplementary capital, is also usable. Possible values include Tier 1, Additional Tier 1, Tier 2, Not Subject to Regulations, and Not Provided.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
