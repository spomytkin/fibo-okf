---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is bank qualified
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: designation given to a public purpose bond offering by the issuer if it reasonably expects to issue in the calendar
      year of such offering no more than $10 million par amount of bonds of the type required to be included in making such
      calculation under the Internal Revenue Code.  When purchased by a commercial bank for its portfolio, the bank may receive
      an 80% tax deduction for the interest cost of carry for the issue.  A bond that is bank qualified is also known as a
      qualified tax-exempt obligation.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/BondOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/BondOffering
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/isBankQualified
sources:
- id: fibo-source-560fdfbe3a
  resource: references/fibo/BP/SecuritiesIssuance/DebtIssuance.rdf
  sha256: 560fdfbe3abab0e0bb6f417a8acec1661acf530aeee87d8a033ef11bbf4af57b
  title: FIBO source BP/SecuritiesIssuance/DebtIssuance.rdf
title: is bank qualified
type: Ontology Property
---

# is bank qualified

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/DebtIssuance/isBankQualified>

## Definition

designation given to a public purpose bond offering by the issuer if it reasonably expects to issue in the calendar year of such offering no more than $10 million par amount of bonds of the type required to be included in making such calculation under the Internal Revenue Code.  When purchased by a commercial bank for its portfolio, the bank may receive an 80% tax deduction for the interest cost of carry for the issue.  A bond that is bank qualified is also known as a qualified tax-exempt obligation.

## Relationships

- **Domain**: [BondOffering](/concepts/fibo/BP/SecuritiesIssuance/DebtIssuance/BondOffering.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label** (en): is bank qualified
- **definition** (en): designation given to a public purpose bond offering by the issuer if it reasonably expects to issue in the calendar year of such offering no more than $10 million par amount of bonds of the type required to be included in making such calculation under the Internal Revenue Code.  When purchased by a commercial bank for its portfolio, the bank may receive an 80% tax deduction for the interest cost of carry for the issue.  A bond that is bank qualified is also known as a qualified tax-exempt obligation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
