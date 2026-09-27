---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: insurance company
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: non-depository institution whose primary and predominant business activity is the writing of insurance or the reinsuring
      of risks underwritten by insurance companies, and that provides compensation based on the happening of at least one
      contingency
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: http://www.ffiec.gov/nicpubweb/Content/HELP/Institution%20Type%20Description.htm
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: https://www.sec.gov/about/laws/ica40.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'In the US, insurance companies are subject to supervision by the insurance commissioner or a similar official
      or agency of a State; or any receiver or similar official or any liquidating agent for such a company, in his capacity
      as such. Common forms of insurance include life, property and casualty, and health insurance. In addition to insuring
      against hazards, many insurance companies also sell investments or investment-like products. The most prevalent investment
      products offered by insurers are annuities and life insurance policies that also feature investment elements.


      A number of insurance companies operate brokerage arms that trade securities on behalf of clients.'
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/RiskPoolingInstitution.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/RiskPoolingInstitution
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InsuranceCompany
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: insurance company
type: Ontology Class
---

# insurance company

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/InsuranceCompany>

## Definition

non-depository institution whose primary and predominant business activity is the writing of insurance or the reinsuring of risks underwritten by insurance companies, and that provides compensation based on the happening of at least one contingency

## Relationships

- **Subclass of**: [RiskPoolingInstitution](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/RiskPoolingInstitution.md)

## Annotations

- **label**: insurance company
- **definition**: non-depository institution whose primary and predominant business activity is the writing of insurance or the reinsuring of risks underwritten by insurance companies, and that provides compensation based on the happening of at least one contingency
- **adaptedFrom**: http://www.ffiec.gov/nicpubweb/Content/HELP/Institution%20Type%20Description.htm
- **adaptedFrom**: https://www.sec.gov/about/laws/ica40.pdf
- **explanatoryNote**: In the US, insurance companies are subject to supervision by the insurance commissioner or a similar official or agency of a State; or any receiver or similar official or any liquidating agent for such a company, in his capacity as such. Common forms of insurance include life, property and casualty, and health insurance. In addition to insuring against hazards, many insurance companies also sell investments or investment-like products. The most prevalent investment products offered by insurers are annuities and life insurance policies that also feature investment elements.  A number of insurance companies operate brokerage arms that trade securities on behalf of clients.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
