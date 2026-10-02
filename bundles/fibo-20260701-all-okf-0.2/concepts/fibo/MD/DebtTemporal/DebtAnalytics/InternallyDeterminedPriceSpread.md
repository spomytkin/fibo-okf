---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: internally determined price spread
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The spread determined internally within the organisation from information available at their own trading desks.
      Further Notes Internal prices within a bank would be determined by surveying their own traders. So e.g. corporate desk
      trades these 30 bonds, get the daily spreads on those at the end of the day and calculate the price. The traders determine
      the pricing during the based on market movements. (this is all for OTC traded bonds, not exchange traded bonds).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtPriceSpread.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/DebtPriceSpread
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/InternallyDeterminedPriceSpread
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: internally determined price spread
type: Ontology Class
---

# internally determined price spread

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/InternallyDeterminedPriceSpread>

## Definition

The spread determined internally within the organisation from information available at their own trading desks. Further Notes Internal prices within a bank would be determined by surveying their own traders. So e.g. corporate desk trades these 30 bonds, get the daily spreads on those at the end of the day and calculate the price. The traders determine the pricing during the based on market movements. (this is all for OTC traded bonds, not exchange traded bonds).

## Relationships

- **Subclass of**: [DebtPriceSpread](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/DebtPriceSpread.md)

## Annotations

- **label** (en): internally determined price spread
- **definition** (en): The spread determined internally within the organisation from information available at their own trading desks. Further Notes Internal prices within a bank would be determined by surveying their own traders. So e.g. corporate desk trades these 30 bonds, get the daily spreads on those at the end of the day and calculate the price. The traders determine the pricing during the based on market movements. (this is all for OTC traded bonds, not exchange traded bonds).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
