---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: bond equivalent yield
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: Yield determined on an equivalent basis to the yield of another bond. This is used to be able to realistically
      compare prices between debt instruments across different markets.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'For example when comparing Treasury with Corp it''s called a Corp Bond Equivalent Yield; when comparing other
      kinds of yields this would be labelled differently. Treasury bills typically in discount rates - that''s one of the
      ways you would compare TB or MM or RePo to BEQ - by changing the day count. Detailed implementation of this: This term
      refers to the type of bond that it is equivalent to, that is the type of bond whose yield is normally determined according
      to the yield calculation method that is used in determining this Bond Equivalent Yield figure. The type of bond in this
      instance is defined in relation to the market on which that bond trades, for example the US Corporate Bond Market.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/EquivalentYieldCalculationMethod
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/isBasedOn
  subclass_of:
  - concept: /concepts/fibo/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield
resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/BondEquivalentYield
sources:
- id: fibo-source-4a5facbded
  resource: references/fibo/MD/DebtTemporal/DebtAnalytics.rdf
  sha256: 4a5facbdedf24373f412662d54858a7e9bb5e857cf4bc60543d124abfb92804a
  title: FIBO source MD/DebtTemporal/DebtAnalytics.rdf
title: bond equivalent yield
type: Ontology Class
---

# bond equivalent yield

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/DebtAnalytics/BondEquivalentYield>

## Definition

Yield determined on an equivalent basis to the yield of another bond. This is used to be able to realistically compare prices between debt instruments across different markets.

## Relationships

- **Subclass of**: [RelativelyDefinedDebtInstrumentYield](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/RelativelyDefinedDebtInstrumentYield.md)

## Constraints

- **[isBasedOn](/concepts/fibo/FBC/DebtAndEquities/Debt/isBasedOn.md)**: some values from of type [EquivalentYieldCalculationMethod](/concepts/fibo/MD/DebtTemporal/DebtAnalytics/EquivalentYieldCalculationMethod.md)

## Annotations

- **label** (en): bond equivalent yield
- **definition** (en): Yield determined on an equivalent basis to the yield of another bond. This is used to be able to realistically compare prices between debt instruments across different markets.
- **explanatoryNote** (en): For example when comparing Treasury with Corp it's called a Corp Bond Equivalent Yield; when comparing other kinds of yields this would be labelled differently. Treasury bills typically in discount rates - that's one of the ways you would compare TB or MM or RePo to BEQ - by changing the day count. Detailed implementation of this: This term refers to the type of bond that it is equivalent to, that is the type of bond whose yield is normally determined according to the yield calculation method that is used in determining this Bond Equivalent Yield figure. The type of bond in this instance is defined in relation to the market on which that bond trades, for example the US Corporate Bond Market.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
