---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: real estate investment trust
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: investment fund that offers shares/units to the public and invests in real estate directly
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/abbreviation
    value: REIT
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code,
      Fourth edition, October 2019
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Real estate investment trusts own, and in most cases operate, income-producing real estate. REITs own many types
      of commercial real estate, ranging from office and apartment buildings to warehouses, hospitals, shopping centers, hotels
      and commercial forests. Some REITs engage in financing real estate.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/BE/Trusts/Trusts/Trust
    kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/hasLegalStructure
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/ManagedInvestment
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/RealEstateInvestmentTrust
sources:
- id: fibo-source-a82c11f42e
  resource: references/fibo/SEC/Funds/Funds.rdf
  sha256: a82c11f42ef79a0f83aeae8434ad054ddef746da9d97126ef3d8923eacf9c275
  title: FIBO source SEC/Funds/Funds.rdf
title: real estate investment trust
type: Ontology Class
---

# real estate investment trust

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Funds/Funds/RealEstateInvestmentTrust>

## Definition

investment fund that offers shares/units to the public and invests in real estate directly

## Relationships

- **Subclass of**: [ManagedInvestment](/concepts/fibo/SEC/Securities/Pools/ManagedInvestment.md)

## Constraints

- **[hasLegalStructure](/concepts/fibo/SEC/Funds/Funds/hasLegalStructure.md)**: some values from of type [Trust](/concepts/fibo/BE/Trusts/Trusts/Trust.md)

## Annotations

- **label** (en): real estate investment trust
- **definition** (en): investment fund that offers shares/units to the public and invests in real estate directly
- **abbreviation** (en): REIT
- **adaptedFrom** (en): ISO 10962:2019 Securities and related financial instruments - Classification of financial instruments (CFI) code, Fourth edition, October 2019
- **explanatoryNote** (en): Real estate investment trusts own, and in most cases operate, income-producing real estate. REITs own many types of commercial real estate, ranging from office and apartment buildings to warehouses, hospitals, shopping centers, hotels and commercial forests. Some REITs engage in financing real estate.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
