---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: make securities available in market
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'What happens here? e.g. notices / marketing (phone calls) Structured Finance: There''s not really notices in the
      newspaper, it''s a very small market and it''s all based on relationships so there''s no public notice. So you would
      get an email from the sales person at the bank who has just closed the deal and is now selling these (this bank is the
      broker/dealer who bought it?) There''s not really much of a secondary market - the initial investors would often hold
      on to these. There is something around Bloomberg - you can go there and see what''s available, if someone has a number
      of notes from a iven tranche, that they are willing to sell. So there''s no transpoarency (!!) Sales would be OTC but
      less transparent e.g. if you look up a normal OTC stock, you would be able to see more of this information, than in
      these (non Agency) MBS issues and other SF. DOES THIS APPLY IN ALL MBS??.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDeal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/isIssueOf
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDealProspectus
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/requires.1
  subclass_of:
  - concept: /concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity
resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/MakeSecuritiesAvailableInMarket
sources:
- id: fibo-source-edaa40050a
  resource: references/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
  sha256: edaa40050a1b847b1cdce90ef56ea2055f56bb1c63d8a51420f5423ce3efce89
  title: FIBO source BP/SecuritiesIssuance/PrivateLabelMBSIssuance.rdf
title: make securities available in market
type: Ontology Class
---

# make securities available in market

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/MakeSecuritiesAvailableInMarket>

## Definition

What happens here? e.g. notices / marketing (phone calls) Structured Finance: There's not really notices in the newspaper, it's a very small market and it's all based on relationships so there's no public notice. So you would get an email from the sales person at the bank who has just closed the deal and is now selling these (this bank is the broker/dealer who bought it?) There's not really much of a secondary market - the initial investors would often hold on to these. There is something around Bloomberg - you can go there and see what's available, if someone has a number of notes from a iven tranche, that they are willing to sell. So there's no transpoarency (!!) Sales would be OTC but less transparent e.g. if you look up a normal OTC stock, you would be able to see more of this information, than in these (non Agency) MBS issues and other SF. DOES THIS APPLY IN ALL MBS??.

## Relationships

- **Subclass of**: [IssuanceProcessActivity](/concepts/fibo/BP/SecuritiesIssuance/IssuanceProcess/IssuanceProcessActivity.md)

## Constraints

- **[isIssueOf](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/isIssueOf.md)**: some values from of type [TranchedMBSDeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDeal.md)
- **[requires.1](/concepts/fibo/BP/SecuritiesIssuance/PrivateLabelMBSIssuance/requires.1.md)**: some values from of type [TranchedMBSDealProspectus](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDealProspectus.md)

## Annotations

- **label** (en): make securities available in market
- **definition** (en): What happens here? e.g. notices / marketing (phone calls) Structured Finance: There's not really notices in the newspaper, it's a very small market and it's all based on relationships so there's no public notice. So you would get an email from the sales person at the bank who has just closed the deal and is now selling these (this bank is the broker/dealer who bought it?) There's not really much of a secondary market - the initial investors would often hold on to these. There is something around Bloomberg - you can go there and see what's available, if someone has a number of notes from a iven tranche, that they are willing to sell. So there's no transpoarency (!!) Sales would be OTC but less transparent e.g. if you look up a normal OTC stock, you would be able to see more of this information, than in these (non Agency) MBS issues and other SF. DOES THIS APPLY IN ALL MBS??.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
