---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: unitized fund
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: pooled investment vehicle in which investors hold units that represent a proportional share of the fund's underlying
      assets, typically used in pensions or insurance-based products
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#example
    value: Examples include authorized unit trusts (AUTs), investment companies with variable capital (ICVCs), and insurance-linked
      unitized funds.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The concept of a 'unitized fund' comes up in the context of the Financial Conduct Authority (FCA)'s framework for
      collective investment schemes (CIS) in the United Kingdom, particularly in the context of authorized unit trusts (AUTs)
      and insurance-based investments.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The differentiator with respect to a unitized fund is that investors hold units, rather than a direct shareholding
      or segregated account.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/CollectiveInvestmentVehicle
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/UnitizedFund
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: unitized fund
type: Ontology Class
---

# unitized fund

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/UnitizedFund>

## Definition

pooled investment vehicle in which investors hold units that represent a proportional share of the fund's underlying assets, typically used in pensions or insurance-based products

## Relationships

- **Subclass of**: [CollectiveInvestmentVehicle](/concepts/fibo/SEC/Securities/Pools/CollectiveInvestmentVehicle.md)

## Annotations

- **label** (en): unitized fund
- **definition** (en): pooled investment vehicle in which investors hold units that represent a proportional share of the fund's underlying assets, typically used in pensions or insurance-based products
- **example** (en): Examples include authorized unit trusts (AUTs), investment companies with variable capital (ICVCs), and insurance-linked unitized funds.
- **explanatoryNote** (en): The concept of a 'unitized fund' comes up in the context of the Financial Conduct Authority (FCA)'s framework for collective investment schemes (CIS) in the United Kingdom, particularly in the context of authorized unit trusts (AUTs) and insurance-based investments.
- **explanatoryNote** (en): The differentiator with respect to a unitized fund is that investors hold units, rather than a direct shareholding or segregated account.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
