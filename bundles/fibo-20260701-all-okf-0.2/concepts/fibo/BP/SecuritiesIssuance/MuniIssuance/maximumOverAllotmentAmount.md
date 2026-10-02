---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: maximum over allotment amount
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The maximum amount that is available as part of providing the over-allotment option.
  domain:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/DebtIssueOverAllotmentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/DebtIssueOverAllotmentTerms
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssueOverAllotmentTerms.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/IssueOverAllotmentTerms
  range:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/maximumOverAllotmentAmount
sources:
- id: fibo-source-1c106070e5
  resource: references/fibo/BP/SecuritiesIssuance/MuniIssuance.rdf
  sha256: 1c106070e511dce04ec6498cc5a5df3f6dba9e882ef25649d5ada289a93e628f
  title: FIBO source BP/SecuritiesIssuance/MuniIssuance.rdf
title: maximum over allotment amount
type: Ontology Property
---

# maximum over allotment amount

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MuniIssuance/maximumOverAllotmentAmount>

## Definition

The maximum amount that is available as part of providing the over-allotment option.

## Relationships

- **Domain**: [DebtIssueOverAllotmentTerms](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/DebtIssueOverAllotmentTerms.md)
- **Domain**: [IssueOverAllotmentTerms](/concepts/fibo/BP/SecuritiesIssuance/MuniIssuance/IssueOverAllotmentTerms.md)
- **Range**: [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)

## Annotations

- **label** (en): maximum over allotment amount
- **definition** (en): The maximum amount that is available as part of providing the over-allotment option.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
