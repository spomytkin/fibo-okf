---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: establishment
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: an enterprise (or part of an enterprise) that operates from a single physical location
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://stats.oecd.org/glossary/detail.asp?ID=857
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.bls.gov/opub/hom/glossary.htm#E
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.statcan.gc.ca/eng/concepts/units
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The physical location of a certain economic activity - for example, a factory, mine, store, or office. An individual
      establishment is generally classified by having one NAICS code associated with it for statistical purposes, whereas
      an enterprise may be classified by multiple NAICS codes. The statistical structure is defined based on the operating
      structure and the accounting data produced by that entity. A given location may only need to publish revenues, whereas
      an operating unit (establishment) has employment statistics, etc. An establishment is defined as a producing unit at
      a single geographical location at which or from which economic activity is conducted and for which, at a minimum, employment
      data are available. In the case of a home-based business, the actual physical location would be specified as two distinct
      institutional units - as a household from a personal living and consumer perspective and as an establishment / operating
      unit due to the statistics required of the business.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/PhysicalAddress
    kind: exact_qualified_cardinality
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Places/Addresses/hasAddress
  - cardinality: 0
    filler: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Enterprise
    kind: min_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Collections/isConstituentOf
  subclass_of:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Establishment
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: establishment
type: Ontology Class
---

# establishment

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Establishment>

## Definition

an enterprise (or part of an enterprise) that operates from a single physical location

## Relationships

- **Subclass of**: [InstitutionalUnit](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InstitutionalUnit.md)

## Constraints

- **[hasAddress](/concepts/fibo/FND/Places/Addresses/hasAddress.md)**: exact qualified cardinality 1 of type [PhysicalAddress](/concepts/fibo/FND/Places/Addresses/PhysicalAddress.md)
- **[isConstituentOf](<https://www.omg.org/spec/Commons/Collections/isConstituentOf>)**: min qualified cardinality 0 of type [Enterprise](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Enterprise.md)

## Annotations

- **label**: establishment
- **definition**: an enterprise (or part of an enterprise) that operates from a single physical location
- **adaptedFrom**: http://stats.oecd.org/glossary/detail.asp?ID=857
- **adaptedFrom**: http://www.bls.gov/opub/hom/glossary.htm#E
- **adaptedFrom**: http://www.statcan.gc.ca/eng/concepts/units
- **explanatoryNote**: The physical location of a certain economic activity - for example, a factory, mine, store, or office. An individual establishment is generally classified by having one NAICS code associated with it for statistical purposes, whereas an enterprise may be classified by multiple NAICS codes. The statistical structure is defined based on the operating structure and the accounting data produced by that entity. A given location may only need to publish revenues, whereas an operating unit (establishment) has employment statistics, etc. An establishment is defined as a producing unit at a single geographical location at which or from which economic activity is conducted and for which, at a minimum, employment data are available. In the case of a home-based business, the actual physical location would be specified as two distinct institutional units - as a household from a personal living and consumer perspective and as an establishment / operating unit due to the statistics required of the business.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
