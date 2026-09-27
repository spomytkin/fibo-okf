---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pass through m b s deal
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An issue of Mortgage Backed Security instruments in which payments on the pool are passed through to investors
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'The cashflows from interest and principal payments on the mortgages in the underlying pool are passed on to investors,
      usually with the deduction of fees in for them of a reduction in a mumber of percentage points or a monetary amount.
      Modeling note: Thinking about this further, and after more PoC reviews, it seems to me that we should simply define
      two kinds of Deal which are Tranched and Pass Thtrough, just below the level of Pool Backed Securities Deal. Investigaiton
      of various SMOs and REMICs and the like suggests that the original PoC term duality shown here (Tranched = Non Agency;
      Pass Through = Agency) is too simplistic.'
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDeal.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDeal
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/AgencyMBSDeal
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/isAlso
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/DebtInstruments/DebtOffering
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/PassThroughMBSDeal
sources:
- id: fibo-source-a5aa66c8b9
  resource: references/fibo/SEC/Debt/CollateralizedDebtObligations.rdf
  sha256: a5aa66c8b98fee8abed9ce7c551e395e57aaf20d005a706aa7c4a7d7a66136bc
  title: FIBO source SEC/Debt/CollateralizedDebtObligations.rdf
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: pass through m b s deal
type: Ontology Class
---

# pass through m b s deal

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/PassThroughMBSDeal>

## Definition

An issue of Mortgage Backed Security instruments in which payments on the pool are passed through to investors

## Relationships

- **Subclass of**: [DebtOffering](/concepts/fibo/SEC/Debt/DebtInstruments/DebtOffering.md)

## Constraints

- **Disjoint with**: [TranchedMBSDeal](/concepts/fibo/SEC/Debt/CollateralizedDebtObligations/TranchedMBSDeal.md)
- **[isAlso](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/isAlso.md)**: some values from of type [AgencyMBSDeal](/concepts/fibo/SEC/Debt/MortgageBackedSecurities/AgencyMBSDeal.md)

## Annotations

- **label** (en): pass through m b s deal
- **definition** (en): An issue of Mortgage Backed Security instruments in which payments on the pool are passed through to investors
- **editorialNote** (en): The cashflows from interest and principal payments on the mortgages in the underlying pool are passed on to investors, usually with the deduction of fees in for them of a reduction in a mumber of percentage points or a monetary amount. Modeling note: Thinking about this further, and after more PoC reviews, it seems to me that we should simply define two kinds of Deal which are Tranched and Pass Thtrough, just below the level of Pool Backed Securities Deal. Investigaiton of various SMOs and REMICs and the like suggests that the original PoC term duality shown here (Tranched = Non Agency; Pass Through = Agency) is too simplistic.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
