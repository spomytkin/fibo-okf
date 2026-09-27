---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: synthetic debt instrument pool funding asset
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: An asset which provides the funding for a synthetic debt instrument pool, as used in a synthetic CDO.
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'From April 28 review session: CDS mechanization: Q: Are the CDS taken out on the constituents of the (non owned)
      pool or on some other instrument? A: There is funding to underpin the pool. The funding may be high grade debt or may
      be low grade. There is an undedrlying source of funds. then you swap (using CDS) into other risks. so I might lend to
      a government institution, and then sell protection against a whole series of corporates. So I''ve taken the high quality
      portfolio and added other risks to it. Or the other way round. conclusions:'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditRatings/InstrumentCreditRating
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/hasInvestmentGrade
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset
sources:
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: synthetic debt instrument pool funding asset
type: Ontology Class
---

# synthetic debt instrument pool funding asset

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticDebtInstrumentPoolFundingAsset>

## Definition

An asset which provides the funding for a synthetic debt instrument pool, as used in a synthetic CDO.

## Additional definitions

- From April 28 review session: CDS mechanization: Q: Are the CDS taken out on the constituents of the (non owned) pool or on some other instrument? A: There is funding to underpin the pool. The funding may be high grade debt or may be low grade. There is an undedrlying source of funds. then you swap (using CDS) into other risks. so I might lend to a government institution, and then sell protection against a whole series of corporates. So I've taken the high quality portfolio and added other risks to it. Or the other way round. conclusions:

## Constraints

- **[hasInvestmentGrade](/concepts/fibo/SEC/Debt/SyntheticCDOs/hasInvestmentGrade.md)**: some values from of type [InstrumentCreditRating](/concepts/fibo/FBC/DebtAndEquities/CreditRatings/InstrumentCreditRating.md)

## Annotations

- **label** (en): synthetic debt instrument pool funding asset
- **definition** (en): An asset which provides the funding for a synthetic debt instrument pool, as used in a synthetic CDO.
- **definition** (en): From April 28 review session: CDS mechanization: Q: Are the CDS taken out on the constituents of the (non owned) pool or on some other instrument? A: There is funding to underpin the pool. The funding may be high grade debt or may be low grade. There is an undedrlying source of funds. then you swap (using CDS) into other risks. so I might lend to a government institution, and then sell protection against a whole series of corporates. So I've taken the high quality portfolio and added other risks to it. Or the other way round. conclusions:

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
