---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: instrument credit rating
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment credit rating that provides an opinion of creditworthiness of an instrument, typically with some relationship
      to the creditworthiness of the issuer(s)
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Ratings/rates
  subclass_of:
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditRatings/InvestmentCreditRating.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/InvestmentCreditRating
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/InstrumentCreditRating
sources:
- id: fibo-source-1f582cd28a
  resource: references/fibo/FBC/DebtAndEquities/CreditRatings.rdf
  sha256: 1f582cd28aa6fc7dddfffeabef7c4aed9e4a1274b09047548096bd1769f759b7
  title: FIBO source FBC/DebtAndEquities/CreditRatings.rdf
title: instrument credit rating
type: Ontology Class
---

# instrument credit rating

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/InstrumentCreditRating>

## Definition

investment credit rating that provides an opinion of creditworthiness of an instrument, typically with some relationship to the creditworthiness of the issuer(s)

## Relationships

- **Subclass of**: [InvestmentCreditRating](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/InvestmentCreditRating.md)

## Constraints

- **[rates](/concepts/fibo/FND/Arrangements/Ratings/rates.md)**: some values from of type [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)

## Annotations

- **label** (en): instrument credit rating
- **definition** (en): investment credit rating that provides an opinion of creditworthiness of an instrument, typically with some relationship to the creditworthiness of the issuer(s)

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
