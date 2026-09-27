---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: tranche notes parameters
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'One set of information defining the notes breakdown of one tranche. Covers denominations and amounts that you
      can byu of the instrument in this tranche. Q: Is this really defined in the prospectus? A: yes The prospectus lists
      the characteristics including e.g. "The notes will be sold in denominations of X AND Increuemtns of Y e.g. $250 000
      incremented by $1000. Parameters include: Denominations Minimum amounts what else? Term origin:MBS PoC Reviews'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/MonetaryAmount
    kind: max_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/maximumAmount
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/MBSTrancheNote
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Documents/isAbout
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TrancheNotesParameters
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: tranche notes parameters
type: Ontology Class
---

# tranche notes parameters

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TrancheNotesParameters>

## Definition

One set of information defining the notes breakdown of one tranche. Covers denominations and amounts that you can byu of the instrument in this tranche. Q: Is this really defined in the prospectus? A: yes The prospectus lists the characteristics including e.g. "The notes will be sold in denominations of X AND Increuemtns of Y e.g. $250 000 incremented by $1000. Parameters include: Denominations Minimum amounts what else? Term origin:MBS PoC Reviews

## Relationships

- **Subclass of**: [TranchedMBSIssueProspectusPart](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/TranchedMBSIssueProspectusPart.md)

## Constraints

- **[maximumAmount](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/maximumAmount.md)**: max qualified cardinality 1 of type [MonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/MonetaryAmount.md)
- **[isAbout](<https://www.omg.org/spec/Commons/Documents/isAbout>)**: some values from of type [MBSTrancheNote](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/MBSTrancheNote.md)

## Annotations

- **label** (en): tranche notes parameters
- **definition** (en): One set of information defining the notes breakdown of one tranche. Covers denominations and amounts that you can byu of the instrument in this tranche. Q: Is this really defined in the prospectus? A: yes The prospectus lists the characteristics including e.g. "The notes will be sold in denominations of X AND Increuemtns of Y e.g. $250 000 incremented by $1000. Parameters include: Denominations Minimum amounts what else? Term origin:MBS PoC Reviews

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
