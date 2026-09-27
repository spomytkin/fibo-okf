---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: arbitrage c d o
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Arbitrage CDO/CLO/CBO - the reference assets are bought by a firm or conduit or SPV (Special Purpose Vehicle) with
      a view to repackage them and sell them on as the structured product.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Arbitrage deals are motivated by the opportunity to add value by repackaging collateral into tranches. This is
      the same motivation for most CMOs. In finance, the law of one price suggests that the securities of a CDO should have
      the same market value as its underlying collateral. In practice, this is often not the case. Accordingly, a CDO can
      represent a theoretical arbitrage. april 28 note: Does this have meaning for Cash CDO? Are these always? Arbitrage is
      there to exploit market inefficiencies. Would there not be some arbitrage exploited in the CDO. The definition here
      implies cash CDO only. not cler to reviewers what the ditinctio nis and whether these are mutually excluive. On eview
      is that the arb CDO has cash inflorws different to cash outflows, e.g. 9.5% v 9% with the 50bp taken as fees. So that
      might be Arb CDO. There is another type we hav emissed: like an arb CDO where there is instead a spread between in/out
      as above, you have instead a MArket Value CDO, where its base don the market value of the deal. Not clear how you are
      supposed to realized that value. you are supposed to realize the xxxx of securities .Seen both referred to. So is arb
      a risk management tool.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ArbitrageCdoObjective
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/hasCDOOriginationObjective
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/CDODeal
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ArbitrageCDO
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
title: arbitrage c d o
type: Ontology Class
---

# arbitrage c d o

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/ArbitrageCDO>

## Definition

Arbitrage CDO/CLO/CBO - the reference assets are bought by a firm or conduit or SPV (Special Purpose Vehicle) with a view to repackage them and sell them on as the structured product.

## Relationships

- **Subclass of**: [CDODeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/CDODeal.md)

## Constraints

- **[hasCDOOriginationObjective](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/hasCDOOriginationObjective.md)**: some values from of type [ArbitrageCdoObjective](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/ArbitrageCdoObjective.md)

## Annotations

- **label** (en): arbitrage c d o
- **definition** (en): Arbitrage CDO/CLO/CBO - the reference assets are bought by a firm or conduit or SPV (Special Purpose Vehicle) with a view to repackage them and sell them on as the structured product.
- **editorialNote** (en): Arbitrage deals are motivated by the opportunity to add value by repackaging collateral into tranches. This is the same motivation for most CMOs. In finance, the law of one price suggests that the securities of a CDO should have the same market value as its underlying collateral. In practice, this is often not the case. Accordingly, a CDO can represent a theoretical arbitrage. april 28 note: Does this have meaning for Cash CDO? Are these always? Arbitrage is there to exploit market inefficiencies. Would there not be some arbitrage exploited in the CDO. The definition here implies cash CDO only. not cler to reviewers what the ditinctio nis and whether these are mutually excluive. On eview is that the arb CDO has cash inflorws different to cash outflows, e.g. 9.5% v 9% with the 50bp taken as fees. So that might be Arb CDO. There is another type we hav emissed: like an arb CDO where there is instead a spread between in/out as above, you have instead a MArket Value CDO, where its base don the market value of the deal. Not clear how you are supposed to realized that value. you are supposed to realize the xxxx of securities .Seen both referred to. So is arb a risk management tool.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
