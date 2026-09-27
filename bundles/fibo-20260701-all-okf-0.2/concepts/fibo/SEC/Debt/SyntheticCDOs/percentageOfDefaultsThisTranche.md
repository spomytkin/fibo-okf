---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: percentage of defaults this tranche
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: 'The percentage of defaults which holders of this are exposed to, that is the percentage of defaults that this
      tranche represents. Further Notes Review session notes 21 April: The first, second and so on, to stop paying out when
      there is a default. In each case you get the first, second etc. x% of defaults. Base underlying may be high or low quality.
      Create the pool by buying or selling protection depending on hich way you want to go, e..g. have high quality funds,
      (borrowers), would sell protection. If low quality, would buy protection to improve quality. So risk is no longer bound
      to the funding. REVIEW: More likely this is a band of percentages (from and to); review and formalize. See also note
      on attachment and detachment points.'
  domain:
  - concept: /concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/percentageOfDefaultsThisTranche
sources:
- id: fibo-source-141b3c40ed
  resource: references/fibo/SEC/Debt/SyntheticCDOs.rdf
  sha256: 141b3c40ed364214aed3965d9cbe9daaa58da12da50f05938bd6d436aad71e2b
  title: FIBO source SEC/Debt/SyntheticCDOs.rdf
title: percentage of defaults this tranche
type: Ontology Property
---

# percentage of defaults this tranche

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/SyntheticCDOs/percentageOfDefaultsThisTranche>

## Definition

The percentage of defaults which holders of this are exposed to, that is the percentage of defaults that this tranche represents. Further Notes Review session notes 21 April: The first, second and so on, to stop paying out when there is a default. In each case you get the first, second etc. x% of defaults. Base underlying may be high or low quality. Create the pool by buying or selling protection depending on hich way you want to go, e..g. have high quality funds, (borrowers), would sell protection. If low quality, would buy protection to improve quality. So risk is no longer bound to the funding. REVIEW: More likely this is a band of percentages (from and to); review and formalize. See also note on attachment and detachment points.

## Relationships

- **Domain**: [SyntheticCDOTranche](/concepts/fibo/SEC/Debt/SyntheticCDOs/SyntheticCDOTranche.md)
- **Range**: [Percentage](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Percentage>)

## Annotations

- **label** (en): percentage of defaults this tranche
- **definition** (en): The percentage of defaults which holders of this are exposed to, that is the percentage of defaults that this tranche represents. Further Notes Review session notes 21 April: The first, second and so on, to stop paying out when there is a default. In each case you get the first, second etc. x% of defaults. Base underlying may be high or low quality. Create the pool by buying or selling protection depending on hich way you want to go, e..g. have high quality funds, (borrowers), would sell protection. If low quality, would buy protection to improve quality. So risk is no longer bound to the funding. REVIEW: More likely this is a band of percentages (from and to); review and formalize. See also note on attachment and detachment points.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
