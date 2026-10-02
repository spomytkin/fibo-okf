---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: listing
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: catalog entry for a securities offering managed by an exchange that provides the terms under which that security
      is made available on that exchange
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: market listing
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/hasLotSize
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus
  - filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/Currency
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasCurrency
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasDelistingDate
  - cardinality: 0
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/DateTime
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasLastTradingDateTime
  - cardinality: 1
    filler: https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasListingDate
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/hasTickSize
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecuritiesOffering
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/lists
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesRestrictions/hasRestriction
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing
sources:
- id: fibo-source-966091c50a
  resource: references/fibo/SEC/Securities/SecuritiesIdentification.rdf
  sha256: 966091c50a68aae0becec1ae82b25a9fa7129356c4caa9b25ba1ed33b8fdd2cf
  title: FIBO source SEC/Securities/SecuritiesIdentification.rdf
- id: fibo-source-b48b0dffba
  resource: references/fibo/SEC/Securities/SecuritiesListings.rdf
  sha256: b48b0dffba0ff38934d4794fc2b405f7381e06bb5593315f94807ca42a5731ae
  title: FIBO source SEC/Securities/SecuritiesListings.rdf
- id: fibo-source-241669b0c1
  resource: references/fibo/SEC/Securities/SecuritiesRestrictions.rdf
  sha256: 241669b0c114de2a69849d3c5ae0b04d6c14efbda13080a5a41e98a49ceef1f2
  title: FIBO source SEC/Securities/SecuritiesRestrictions.rdf
title: listing
type: Ontology Class
---

# listing

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesListings/Listing>

## Definition

catalog entry for a securities offering managed by an exchange that provides the terms under which that security is made available on that exchange

## Relationships

- **Subclass of**: [SecurityRegistryEntry](/concepts/fibo/SEC/Securities/SecuritiesIdentification/SecurityRegistryEntry.md)

## Constraints

- **[hasLotSize](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/hasLotSize.md)**: min qualified cardinality 0 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)
- **[hasRegistrationStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/hasRegistrationStatus.md)**: max qualified cardinality 1 of type [RegistrationStatus](/concepts/fibo/FBC/FunctionalEntities/BusinessRegistries/RegistrationStatus.md)
- **[hasCurrency](/concepts/fibo/FND/Accounting/CurrencyAmount/hasCurrency.md)**: some values from of type [Currency](/concepts/fibo/FND/Accounting/CurrencyAmount/Currency.md)
- **[hasDelistingDate](/concepts/fibo/SEC/Securities/SecuritiesListings/hasDelistingDate.md)**: min qualified cardinality 0 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[hasLastTradingDateTime](/concepts/fibo/SEC/Securities/SecuritiesListings/hasLastTradingDateTime.md)**: min qualified cardinality 0 of type [DateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/DateTime>)
- **[hasListingDate](/concepts/fibo/SEC/Securities/SecuritiesListings/hasListingDate.md)**: exact qualified cardinality 1 of type [CombinedDateTime](<https://www.omg.org/spec/Commons/DatesAndTimes/CombinedDateTime>)
- **[hasTickSize](/concepts/fibo/SEC/Securities/SecuritiesListings/hasTickSize.md)**: min qualified cardinality 0 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[lists](/concepts/fibo/SEC/Securities/SecuritiesListings/lists.md)**: exact qualified cardinality 1 of type [SecuritiesOffering](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecuritiesOffering.md)
- **[hasRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/hasRestriction.md)**: min qualified cardinality 0 of type [SecuritiesRestriction](/concepts/fibo/SEC/Securities/SecuritiesRestrictions/SecuritiesRestriction.md)

## Annotations

- **label** (en): listing
- **definition**: catalog entry for a securities offering managed by an exchange that provides the terms under which that security is made available on that exchange
- **synonym** (en): market listing

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
