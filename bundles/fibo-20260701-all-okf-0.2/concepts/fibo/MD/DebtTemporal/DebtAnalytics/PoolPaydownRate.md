---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: pool paydown rate
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The rate at which the pool is paying down. This is based on observed factor. CPR, SMM, etc. etc. Measured differently
      for different kinds of security. CBO might have a prepayment rate for example if the underlying bond is callable. with
      a non agency mortgge dela, defualts will effect this. so for instance there is principal is no lnger inthe pool because
      the mortgagee defaults. With agency these are not taken out in the case of default but for non agency these mortgages
      are removed from the pool if and when a mortgagee defualts.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolFactor
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  - cardinality: 1
    filler: http://www.w3.org/2001/XMLSchema#decimal
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/hasRateValue
  subclass_of:
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/QuantitiesAndUnits/Ratio
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolPaydownRate
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: pool paydown rate
type: Ontology Class
---

# pool paydown rate

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/PoolPaydownRate>

## Definition

The rate at which the pool is paying down. This is based on observed factor. CPR, SMM, etc. etc. Measured differently for different kinds of security. CBO might have a prepayment rate for example if the underlying bond is callable. with a non agency mortgge dela, defualts will effect this. so for instance there is principal is no lnger inthe pool because the mortgagee defaults. With agency these are not taken out in the case of default but for non agency these mortgages are removed from the pool if and when a mortgagee defualts.

## Relationships

- **Subclass of**: [Ratio](<https://www.omg.org/spec/Commons/QuantitiesAndUnits/Ratio>)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [PoolFactor](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/PoolFactor.md)
- **[hasRateValue](/concepts/fibo/FND/Accounting/CurrencyAmount/hasRateValue.md)**: exact qualified cardinality 1 of type [decimal](<http://www.w3.org/2001/XMLSchema#decimal>)

## Annotations

- **label** (en): pool paydown rate
- **definition** (en): The rate at which the pool is paying down. This is based on observed factor. CPR, SMM, etc. etc. Measured differently for different kinds of security. CBO might have a prepayment rate for example if the underlying bond is callable. with a non agency mortgge dela, defualts will effect this. so for instance there is principal is no lnger inthe pool because the mortgagee defaults. With agency these are not taken out in the case of default but for non agency these mortgages are removed from the pool if and when a mortgagee defualts.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
