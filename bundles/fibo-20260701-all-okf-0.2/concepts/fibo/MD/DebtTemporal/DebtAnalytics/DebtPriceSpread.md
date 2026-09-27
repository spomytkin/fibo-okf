---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: debt price spread
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The difference between the [what?] of a security and the fair price value of a different security which is used
      as a point of reference. The spread is used to determine the price of the instrument. (draft definition)
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'This was "Spread" in the Debt pricing reviews, however that word has at least 2 other uses (spread between equity
      bid and offer prices; spread for derivatives). Detailed notes from Debt Pricing Review session 5 Aug: Identify what
      the spread is in relation to e.g. LIBOR. ALSO If fixed of floating. So if it''s a FRN, For a fixed rate bond, it''s
      priced off the on-the-run, e.g. a 30 year bond is priced as a spread wrt a 30 year treasury bond. So e..g spread would
      be something like 10bp+the value of the 30 year on the run Treasury. On the Run: definition needed. Also class of Thing
      and where this should go.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo
  subclass_of:
  - concept: /concepts/fibo/IND/Indicators/Indicators/MarketSpread.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/Indicators/Indicators/MarketSpread
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtPriceSpread
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: debt price spread
type: Ontology Class
---

# debt price spread

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtPriceSpread>

## Definition

The difference between the [what?] of a security and the fair price value of a different security which is used as a point of reference. The spread is used to determine the price of the instrument. (draft definition)

## Relationships

- **Subclass of**: [MarketSpread](/concepts/fibo/IND/Indicators/Indicators/MarketSpread.md)

## Constraints

- **[appliesTo](<https://www.omg.org/spec/Commons/ContextualDesignators/appliesTo>)**: some values from of type [SecurityPrice](/concepts/fibo/FBC/FinancialInstruments/InstrumentPricing/SecurityPrice.md)

## Annotations

- **label** (en): debt price spread
- **definition** (en): The difference between the [what?] of a security and the fair price value of a different security which is used as a point of reference. The spread is used to determine the price of the instrument. (draft definition)
- **editorialNote** (en): This was "Spread" in the Debt pricing reviews, however that word has at least 2 other uses (spread between equity bid and offer prices; spread for derivatives). Detailed notes from Debt Pricing Review session 5 Aug: Identify what the spread is in relation to e.g. LIBOR. ALSO If fixed of floating. So if it's a FRN, For a fixed rate bond, it's priced off the on-the-run, e.g. a 30 year bond is priced as a spread wrt a 30 year treasury bond. So e..g spread would be something like 10bp+the value of the 30 year on the run Treasury. On the Run: definition needed. Also class of Thing and where this should go.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
