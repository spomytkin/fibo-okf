---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: MiFID regulated security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: security for which MiFID reporting is required
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A MiFID requlated security is one that is traded on a MiFID regulated market and for which certain additional reporting
      requirements apply. Markets in Financial Instruments Directive (MiFID), which is a European regulation, issued by the
      European Securities and Markets Authority (ESMA), that aims to increase transparency across the European Union's financial
      markets and standardize regulatory disclosures required for firms operating within the EU.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/hasUpperLimitOnFloatingShares
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/isMiFIDReportingRequired
    value: 'true'
  subclass_of:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/MiFIDRegulatedSecurity
sources:
- id: fibo-source-d2c4e0b02d
  resource: references/fibo/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.rdf
  sha256: d2c4e0b02d30114692ca293e6f51e26b36eef9f530171ac73c4831c6e7869087
  title: FIBO source SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions.rdf
title: MiFID regulated security
type: Ontology Class
---

# MiFID regulated security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/MiFIDRegulatedSecurity>

## Definition

security for which MiFID reporting is required

## Relationships

- **Subclass of**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)

## Constraints

- **[hasUpperLimitOnFloatingShares](/concepts/fibo/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/hasUpperLimitOnFloatingShares.md)**: min qualified cardinality 0 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[isMiFIDReportingRequired](/concepts/fibo/SEC/Securities/EuropeanSecurities/EUSecuritiesRestrictions/isMiFIDReportingRequired.md)**: has value value `true`

## Annotations

- **label** (en): MiFID regulated security
- **definition** (en): security for which MiFID reporting is required
- **explanatoryNote**: A MiFID requlated security is one that is traded on a MiFID regulated market and for which certain additional reporting requirements apply. Markets in Financial Instruments Directive (MiFID), which is a European regulation, issued by the European Securities and Markets Authority (ESMA), that aims to increase transparency across the European Union's financial markets and standardize regulatory disclosures required for firms operating within the EU.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
