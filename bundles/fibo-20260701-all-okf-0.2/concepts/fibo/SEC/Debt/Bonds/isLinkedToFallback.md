---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is linked to fallback
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: relates an index-linked instrument to a government bond that may be selected by a calculation agent
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Fallback Bond means, in relation to an Inflation Index applicable to an Inflation Linked Note, a bond selected
      by the Calculation Agent and issued by the government or one of the governments (but not any government agency) of the
      country (or countries) to whose level of inflation the Inflation Index relates and which pays a coupon and/or redemption
      amount which is calculated by reference to the Inflation Index, with a maturity date which falls on the same day as
      the Maturity Date of the Inflation Linked Notes, or such other date as the Calculation Agent shall select if there is
      no such bond maturing on the Maturity Date of the Inflation Linked Notes. If any bond so selected is redeemed, the Calculation
      Agent will select a new Fallback Bond on the same basis, but selected from all eligible bonds in issue at the time the
      original Fallback Bond is redeemed (including any bond for which the redeemed bond is exchanged). Note the rate of the
      fallback bond is used as a substitute for the inflation index if, for example, it is no longer published.
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument
  range:
  - concept: /concepts/fibo/SEC/Debt/Bonds/GovernmentBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentBond
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://www.omg.org/spec/Commons/Documents/refersTo
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isLinkedToFallback
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: is linked to fallback
type: Ontology Property
---

# is linked to fallback

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isLinkedToFallback>

## Definition

relates an index-linked instrument to a government bond that may be selected by a calculation agent

## Relationships

- **Domain**: [FinancialInstrument](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/FinancialInstrument.md)
- **Range**: [GovernmentBond](/concepts/fibo/SEC/Debt/Bonds/GovernmentBond.md)
- **Subproperty of**: [refersTo](<https://www.omg.org/spec/Commons/Documents/refersTo>)

## Annotations

- **label**: is linked to fallback
- **definition**: relates an index-linked instrument to a government bond that may be selected by a calculation agent
- **explanatoryNote**: Fallback Bond means, in relation to an Inflation Index applicable to an Inflation Linked Note, a bond selected by the Calculation Agent and issued by the government or one of the governments (but not any government agency) of the country (or countries) to whose level of inflation the Inflation Index relates and which pays a coupon and/or redemption amount which is calculated by reference to the Inflation Index, with a maturity date which falls on the same day as the Maturity Date of the Inflation Linked Notes, or such other date as the Calculation Agent shall select if there is no such bond maturing on the Maturity Date of the Inflation Linked Notes. If any bond so selected is redeemed, the Calculation Agent will select a new Fallback Bond on the same basis, but selected from all eligible bonds in issue at the time the original Fallback Bond is redeemed (including any bond for which the redeemed bond is exchanged). Note the rate of the fallback bond is used as a substitute for the inflation index if, for example, it is no longer published.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
