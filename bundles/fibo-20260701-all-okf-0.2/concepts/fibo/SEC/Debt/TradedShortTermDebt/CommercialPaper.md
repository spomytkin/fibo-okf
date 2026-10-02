---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: commercial paper
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an unsecured short-term debt instrument typically issued by a bank, corporation, or foreign government to obtain
      funds to meet short-term debt obligations, such as accounts receivable, inventories, or payroll, backed only by an issuing
      bank or company promise to pay the face amount on the maturity date specified on the note
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Commercial paper has a very-short to short maturity period (usually, 2 to 30 days, and rarely more than 270 days).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/AtADiscount
  - kind: has_value
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity
    value: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/CommercialPaper
sources:
- id: fibo-source-5edf240c05
  resource: references/fibo/SEC/Debt/TradedShortTermDebt.rdf
  sha256: 5edf240c05ec5ae1a2890d6bacd728412073d70868c0908cad8aaea54d9d21bf
  title: FIBO source SEC/Debt/TradedShortTermDebt.rdf
title: commercial paper
type: Ontology Class
---

# commercial paper

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/TradedShortTermDebt/CommercialPaper>

## Definition

an unsecured short-term debt instrument typically issued by a bank, corporation, or foreign government to obtain funds to meet short-term debt obligations, such as accounts receivable, inventories, or payroll, backed only by an issuing bank or company promise to pay the face amount on the maturity date specified on the note

## Relationships

- **Subclass of**: [MoneyMarketInstrument](/concepts/fibo/SEC/Debt/TradedShortTermDebt/MoneyMarketInstrument.md)

## Constraints

- **[hasRelativePriceAtIssue](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtIssue.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/AtADiscount`
- **[hasRelativePriceAtMaturity](/concepts/fibo/SEC/Debt/DebtInstruments/hasRelativePriceAtMaturity.md)**: has value value `https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/ParValue`

## Annotations

- **label** (en): commercial paper
- **definition** (en): an unsecured short-term debt instrument typically issued by a bank, corporation, or foreign government to obtain funds to meet short-term debt obligations, such as accounts receivable, inventories, or payroll, backed only by an issuing bank or company promise to pay the face amount on the maturity date specified on the note
- **explanatoryNote** (en): Commercial paper has a very-short to short maturity period (usually, 2 to 30 days, and rarely more than 270 days).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
