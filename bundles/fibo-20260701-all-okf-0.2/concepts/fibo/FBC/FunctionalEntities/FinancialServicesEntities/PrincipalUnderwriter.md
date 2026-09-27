---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: principal underwriter
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: underwriter who, as principal, purchases from an investment company, or pursuant to some contract has the right
      to purchase from such company, any security for distribution, or who as agent for such company sells or has the right
      to sell any security to a dealer or to the public, excluding any dealer who purchases from such company through sn underwriter
      acting as an agent for such company
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: Section 3a of the Investment Company Act of 1940 as amended in January, 2012, https://www.sec.gov/about/laws/ica40.pdf
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Principal underwriter of or for a closed-end company or any issuer which is not an investment company, or of any
      security issued by such a company or issuer, means any underwriter who, in connection with a primary distribution of
      securities, (a) is in privity of contract with the issuer or an affiliated person of the issuer; (b) acting alone or
      in concert with one or more other persons, initiates or directs the formation of an underwriting syndicate; or (c) is
      allowed a rate of gross commission, spread, or other profit greater than the rate allowed another underwriter participating
      in the distribution.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/PrincipalUnderwriter
sources:
- id: fibo-source-6e6990f74b
  resource: references/fibo/FBC/FunctionalEntities/FinancialServicesEntities.rdf
  sha256: 6e6990f74b40d4b0500a945cb9492927f845764329794290952c527016de49c1
  title: FIBO source FBC/FunctionalEntities/FinancialServicesEntities.rdf
title: principal underwriter
type: Ontology Class
---

# principal underwriter

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/PrincipalUnderwriter>

## Definition

underwriter who, as principal, purchases from an investment company, or pursuant to some contract has the right to purchase from such company, any security for distribution, or who as agent for such company sells or has the right to sell any security to a dealer or to the public, excluding any dealer who purchases from such company through sn underwriter acting as an agent for such company

## Relationships

- **Subclass of**: [Underwriter](/concepts/fibo/FBC/FunctionalEntities/FinancialServicesEntities/Underwriter.md)

## Annotations

- **label**: principal underwriter
- **definition**: underwriter who, as principal, purchases from an investment company, or pursuant to some contract has the right to purchase from such company, any security for distribution, or who as agent for such company sells or has the right to sell any security to a dealer or to the public, excluding any dealer who purchases from such company through sn underwriter acting as an agent for such company
- **adaptedFrom**: Section 3a of the Investment Company Act of 1940 as amended in January, 2012, https://www.sec.gov/about/laws/ica40.pdf
- **explanatoryNote**: Principal underwriter of or for a closed-end company or any issuer which is not an investment company, or of any security issued by such a company or issuer, means any underwriter who, in connection with a primary distribution of securities, (a) is in privity of contract with the issuer or an affiliated person of the issuer; (b) acting alone or in concert with one or more other persons, initiates or directs the formation of an underwriting syndicate; or (c) is allowed a rate of gross commission, spread, or other profit greater than the rate allowed another underwriter participating in the distribution.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
