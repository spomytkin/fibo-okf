---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: principal
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'with respect to a debt: the value of an obligation, such as a bond or loan, raised and that must be repaid at
      maturity; for investments: the original amount of money invested, separate from any associated interest, dividends or
      capital gains'
  defined_by:
  - concept: /concepts/fibo/FBC/DebtAndEquities/Debt.md
    predicate: http://www.w3.org/2000/01/rdf-schema#isDefinedBy
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Debt
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isPrincipalOf
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.finra.org/investors/bond-glossary#p
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Classifiers/Aspect
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Principal
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: principal
type: Ontology Class
---

# principal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Principal>

## Definition

with respect to a debt: the value of an obligation, such as a bond or loan, raised and that must be repaid at maturity; for investments: the original amount of money invested, separate from any associated interest, dividends or capital gains

## Relationships

- **Defined by**: [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt.md)
- **See also**: [p](<http://www.finra.org/investors/bond-glossary#p>)
- **Subclass of**: [Aspect](<https://www.omg.org/spec/Commons/Classifiers/Aspect>)

## Constraints

- **[isPrincipalOf](/concepts/fibo/FBC/DebtAndEquities/Debt/isPrincipalOf.md)**: some values from of type [Debt](/concepts/fibo/FBC/DebtAndEquities/Debt/Debt.md)

## Annotations

- **label**: principal
- **definition**: with respect to a debt: the value of an obligation, such as a bond or loan, raised and that must be repaid at maturity; for investments: the original amount of money invested, separate from any associated interest, dividends or capital gains

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
