---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: synthetic c d o portfolio
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Review notes: What real stuff is this made of? Would be the actual contracts (the Ref Obligation contracts or
      the CDS contract)? Buyer of protection is buying protection and paying a fee. Similar to shorting on a stock. Seller
      of the protection is the one creating the instruments. So the Protection Seller is using the synthetic CDO as some kind
      of synthetic vehicle. Inside the portfolio is the actual contract that generates the cash.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDOPortfolioConstituent
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/notionallyHolds
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDOPortfolio
sources:
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: synthetic c d o portfolio
type: Ontology Class
---

# synthetic c d o portfolio

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDOPortfolio>

## Constraints

- **[notionallyHolds](/concepts/fibo/SEC/Debt/SyntheticCDOs/notionallyHolds.md)**: some values from of type [SyntheticCDOPortfolioConstituent](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOPortfolioConstituent.md)

## Annotations

- **label** (en): synthetic c d o portfolio
- **editorialNote** (en): Review notes: What real stuff is this made of? Would be the actual contracts (the Ref Obligation contracts or the CDS contract)? Buyer of protection is buying protection and paying a fee. Similar to shorting on a stock. Seller of the protection is the one creating the instruments. So the Protection Seller is using the synthetic CDO as some kind of synthetic vehicle. Inside the portfolio is the actual contract that generates the cash.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
