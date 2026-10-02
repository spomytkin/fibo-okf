---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: civilian non-institutional person
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: legal working-age person that does not live in an institution (for example, a correctional facility, long-term
      care hospital, or nursing home), and is not on active military duty
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The working-age population is the total population in a region, within a set range of ages, that is considered
      to be able and likely to work. The working-age population measure is used to give an estimate of the total number of
      potential workers within an economy. For example, in the U.S., it is 16, whereas in Canada it is 15.
  disjoint_with:
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InstitutionalPerson.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/InstitutionalPerson
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: http://www.investopedia.com/terms/w/working-age-population.asp
  subclass_of:
  - concept: /concepts/fibo/FND/AgentsAndPeople/People/LegalWorkingAgePerson.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/AgentsAndPeople/People/LegalWorkingAgePerson
  - concept: /concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Civilian.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/Civilian
resource: https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPerson
sources:
- id: fibo-source-8403bfa401
  resource: references/fibo/IND/EconomicIndicators/EconomicIndicators.rdf
  sha256: 8403bfa40177c207d84c314ab9dc8e157b1928c8ac8b2d5ba84d9260106576c5
  title: FIBO source IND/EconomicIndicators/EconomicIndicators.rdf
title: civilian non-institutional person
type: Ontology Class
---

# civilian non-institutional person

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/IND/EconomicIndicators/EconomicIndicators/CivilianNonInstitutionalPerson>

## Definition

legal working-age person that does not live in an institution (for example, a correctional facility, long-term care hospital, or nursing home), and is not on active military duty

## Relationships

- **See also**: [working-age-population.asp](<http://www.investopedia.com/terms/w/working-age-population.asp>)
- **Subclass of**: [LegalWorkingAgePerson](/concepts/fibo/FND/AgentsAndPeople/People/LegalWorkingAgePerson.md)
- **Subclass of**: [Civilian](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/Civilian.md)

## Constraints

- **Disjoint with**: [InstitutionalPerson](/concepts/fibo/IND/EconomicIndicators/EconomicIndicators/InstitutionalPerson.md)

## Annotations

- **label**: civilian non-institutional person
- **definition**: legal working-age person that does not live in an institution (for example, a correctional facility, long-term care hospital, or nursing home), and is not on active military duty
- **adaptedFrom**: U.S. Bureau of Labor Statistics and Statistics Canada reference definitions - https://wiki.edmcouncil.org/pages/viewpage.action?pageId=6358041
- **explanatoryNote**: The working-age population is the total population in a region, within a set range of ages, that is considered to be able and likely to work. The working-age population measure is used to give an estimate of the total number of potential workers within an economy. For example, in the U.S., it is 16, whereas in Canada it is 15.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
