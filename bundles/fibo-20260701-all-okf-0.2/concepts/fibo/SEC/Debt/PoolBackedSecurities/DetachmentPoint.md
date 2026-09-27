---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: detachment point
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: upper tranche boundary of a tranche defined as a percentage of the value of the total pool of collateral, either
      at issuance or as of some point in time
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: 'Alexander Veremyev, Peter Tsyurmasto, and Stan Uryasev. "Optimal Structuring of CDO contracts: Optimization Approach".
      https://www.ise.ufl.edu/uryasev/files/2012/10/structuring_CDO_JCR_oct12.pdf'
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://fincyclopedia.net/finance/
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The CDO tranche loss arises when the cumulative collateral loss exceeds the tranche's attachment point. The detachment
      point corresponds to the amount of pool losses that will completely wipe out the respective tranche. The detachment
      point is the maximum of pool-level losses at which a given tranche becomes liable for losses.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate
    kind: min_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Arrangements/Assessments/isEstimatedValueOf
  subclass_of:
  - concept: /concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DetachmentPoint
sources:
- id: fibo-source-4922b5d6fd
  resource: references/fibo/SEC/Debt/PoolBackedSecurities.rdf
  sha256: 4922b5d6fd80f046fedb705a51e5978f5d67d714330601c4fa251be149c7b5c7
  title: FIBO source SEC/Debt/PoolBackedSecurities.rdf
title: detachment point
type: Ontology Class
---

# detachment point

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/PoolBackedSecurities/DetachmentPoint>

## Definition

upper tranche boundary of a tranche defined as a percentage of the value of the total pool of collateral, either at issuance or as of some point in time

## Relationships

- **Subclass of**: [PercentageMonetaryAmount](/concepts/fibo/FND/Accounting/CurrencyAmount/PercentageMonetaryAmount.md)

## Constraints

- **[isEstimatedValueOf](/concepts/fibo/FND/Arrangements/Assessments/isEstimatedValueOf.md)**: min qualified cardinality 0 of type [CollateralValueAsOfDate](/concepts/fibo/FBC/DebtAndEquities/Debt/CollateralValueAsOfDate.md)

## Annotations

- **label** (en): detachment point
- **definition** (en): upper tranche boundary of a tranche defined as a percentage of the value of the total pool of collateral, either at issuance or as of some point in time
- **adaptedFrom** (en): Alexander Veremyev, Peter Tsyurmasto, and Stan Uryasev. "Optimal Structuring of CDO contracts: Optimization Approach". https://www.ise.ufl.edu/uryasev/files/2012/10/structuring_CDO_JCR_oct12.pdf
- **adaptedFrom** (en): https://fincyclopedia.net/finance/
- **explanatoryNote** (en): The CDO tranche loss arises when the cumulative collateral loss exceeds the tranche's attachment point. The detachment point corresponds to the amount of pool losses that will completely wipe out the respective tranche. The detachment point is the maximum of pool-level losses at which a given tranche becomes liable for losses.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
