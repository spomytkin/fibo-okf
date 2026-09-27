---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: native yield
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: The yield of the security as determined using the Yield Calculation Method that is the default for the market that
      the security is traded in.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: conventional yield for that security type and geo location, ie. would be in relation too
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NativeYieldCalculationMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NativeYield
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: native yield
type: Ontology Class
---

# native yield

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/NativeYield>

## Definition

The yield of the security as determined using the Yield Calculation Method that is the default for the market that the security is traded in.

## Relationships

- **Subclass of**: [RelativelyDefinedDebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [NativeYieldCalculationMethod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/NativeYieldCalculationMethod.md)

## Annotations

- **label** (en): native yield
- **definition** (en): The yield of the security as determined using the Yield Calculation Method that is the default for the market that the security is traded in.
- **explanatoryNote** (en): conventional yield for that security type and geo location, ie. would be in relation too

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
