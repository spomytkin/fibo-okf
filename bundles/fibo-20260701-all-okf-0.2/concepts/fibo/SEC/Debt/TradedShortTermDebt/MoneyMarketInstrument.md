---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: money market instrument
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: a short-term debt security that gives the owner the unconditional right to receive a stated, fixed sum of money
      on a specified date
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://stats.oecd.org/glossary/detail.asp?ID=6073
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These instruments usually are traded at a discount in organized markets; the discount is dependent upon the interest
      rate and the time remaining to maturity. Included are such instruments as treasury bills, commercial and financial paper,
      bankers' acceptances, negotiable certificates of deposit (with original maturities of one year or less), and short-term
      notes issued under note issuance facilities.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/FixedIncomeSecurity
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument
sources:
- id: fibo-source-5edf240c05
  resource: references/fibo/SEC/Debt/TradedShortTermDebt.rdf
  sha256: 5edf240c05ec5ae1a2890d6bacd728412073d70868c0908cad8aaea54d9d21bf
  title: FIBO source SEC/Debt/TradedShortTermDebt.rdf
title: money market instrument
type: Ontology Class
---

# money market instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument>

## Definition

a short-term debt security that gives the owner the unconditional right to receive a stated, fixed sum of money on a specified date

## Relationships

- **Subclass of**: [FixedIncomeSecurity](/concepts/fibo/SEC/Debt/DebtInstruments/FixedIncomeSecurity.md)

## Annotations

- **label** (en): money market instrument
- **definition** (en): a short-term debt security that gives the owner the unconditional right to receive a stated, fixed sum of money on a specified date
- **adaptedFrom**: https://stats.oecd.org/glossary/detail.asp?ID=6073
- **explanatoryNote** (en): These instruments usually are traded at a discount in organized markets; the discount is dependent upon the interest rate and the time remaining to maturity. Included are such instruments as treasury bills, commercial and financial paper, bankers' acceptances, negotiable certificates of deposit (with original maturities of one year or less), and short-term notes issued under note issuance facilities.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
