---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: mortgage pool
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: loan pool consisting of mortgages that are held in trust as collateral for the issuance of a mortgage-backed security
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: 'Analytics review session notes: Dated facts (for non agency mortgage pools): Aggregate of : Scheduled payments
      (% and $) Payments Prepayments (% and $ notional) Default amounts (statistics: Prepayments: (start at 0 and ramp up
      and then level off (why?)) SMM basic measure monthly Basis CPR C? Prepayment Rate based on SMM annualised PSA based
      on CPR takes the COR and applies a curve to the rate of prepayments on the model. (%) e.g. 100% PSA is applied to model.
      200% PSA implies x%CPR per month Tries to reflect how prepayments in a pool will accelerate and then burn out. This
      reflects the nature of a mortgage pool, elgl why people will prepay, refinance, address selection and so on i.e. local
      economy facts. so those will drop out of the pool and you are left with those who will not. that''s why it levels off.
      So who originates these figures? Is it measured ongoing?: No . Used to determine a pricing speed when marketing the
      security to investors. So this is part of the primary market / issuance where there is marketing. These are the estimated
      figures as they will be at issue. PSA may also be used as triggers. 100 - 400% PSA band - if you go outside that band,
      may change payment behaviour of those classes. Defaults: measures or rate of default CDR conditional default rate (annual)
      MDR Monhtly default rate - like CPR = Rate over time. - both defined as Rates. (%) Figures are originated by the servicer
      of the debt pool. Each serviceer will have their own formats but will do info on prepayments, llosses, detauls on specific
      loans and so on.'
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#editorialNote
    value: "The class Mortgage Pool originally had a property 'pool type' referring to a selection list of textual stylings\
      \ of pool types. Those are now replaced with actual sub types of mortgage pool. Here are the original notes and definition\
      \ that went with the enumerated list of pool types: \n\nThe type of pool for a pool backed security. Each of these pool\
      \ types represents pools of mortgages that have conformed to certain standards (that change periodically) that make\
      \ them \"conforming\" -- such as mortgage balance under a certain threshold, creditworthiness, loan-to-value, etc.\n\
      \nFurther Notes:\nNon Agency signifies a tranched security, for which there will also be a Tranche Type for the security\
      \ tranche itself. All other pool types are Agency pool types. \n\nList Populated from Cutter document Page 5. \n\nAdditional\
      \ terms from Adept Advistory:\nUnder Agency mortgages, basically you have various types of pools under the various agencies.\
      \ You have:\n-GNMA-I\n-GNMA-II\n-GNMA Platinum\n-FNMA \n-FHLMC\n-FHLMC Gold\nAs far as definitions:The simple definition\
      \ is that each of these pool types represents pools of mortgages that have conformed to certain standards (that change\
      \ periodically) that make them \"conforming\" -- such as mortgage balance under a certain threshold, creditworthiness,\
      \ loan-to-value, etc. Also, GNMA is explicitly backed by the US government, while FNMA and FHLMC are only implicitly\
      \ backed by the US government. Perhaps there needs to be some research done on the parameters for what makes a loan\
      \ conforming or not. \n\nConsensus:Review."
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - filler: https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate
    kind: some_values_from
    property: https://www.omg.org/spec/Commons/Collections/hasMember
  subclass_of:
  - concept: /concepts/fibo/SEC/Securities/Pools/DebtPool.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Pools/DebtPool
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgagePool
sources:
- id: fibo-source-025d7e8955
  resource: references/fibo/SEC/Debt/MortgageBackedSecurities.rdf
  sha256: 025d7e89558a319cbd2b60f6a11ca228190a5137c59ed5b5bf34878c5f976f60
  title: FIBO source SEC/Debt/MortgageBackedSecurities.rdf
title: mortgage pool
type: Ontology Class
---

# mortgage pool

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/MortgageBackedSecurities/MortgagePool>

## Definition

loan pool consisting of mortgages that are held in trust as collateral for the issuance of a mortgage-backed security

## Relationships

- **Subclass of**: [DebtPool](/concepts/fibo/SEC/Securities/Pools/DebtPool.md)

## Constraints

- **[hasMember](<https://www.omg.org/spec/Commons/Collections/hasMember>)**: some values from of type [LoanSecuredByRealEstate](/concepts/fibo/LOAN/RealEstateLoans/Mortgages/LoanSecuredByRealEstate.md)

## Annotations

- **label** (en): mortgage pool
- **definition** (en): loan pool consisting of mortgages that are held in trust as collateral for the issuance of a mortgage-backed security
- **editorialNote** (en): Analytics review session notes: Dated facts (for non agency mortgage pools): Aggregate of : Scheduled payments (% and $) Payments Prepayments (% and $ notional) Default amounts (statistics: Prepayments: (start at 0 and ramp up and then level off (why?)) SMM basic measure monthly Basis CPR C? Prepayment Rate based on SMM annualised PSA based on CPR takes the COR and applies a curve to the rate of prepayments on the model. (%) e.g. 100% PSA is applied to model. 200% PSA implies x%CPR per month Tries to reflect how prepayments in a pool will accelerate and then burn out. This reflects the nature of a mortgage pool, elgl why people will prepay, refinance, address selection and so on i.e. local economy facts. so those will drop out of the pool and you are left with those who will not. that's why it levels off. So who originates these figures? Is it measured ongoing?: No . Used to determine a pricing speed when marketing the security to investors. So this is part of the primary market / issuance where there is marketing. These are the estimated figures as they will be at issue. PSA may also be used as triggers. 100 - 400% PSA band - if you go outside that band, may change payment behaviour of those classes. Defaults: measures or rate of default CDR conditional default rate (annual) MDR Monhtly default rate - like CPR = Rate over time. - both defined as Rates. (%) Figures are originated by the servicer of the debt pool. Each serviceer will have their own formats but will do info on prepayments, llosses, detauls on specific loans and so on.
- **editorialNote** (en): The class Mortgage Pool originally had a property 'pool type' referring to a selection list of textual stylings of pool types. Those are now replaced with actual sub types of mortgage pool. Here are the original notes and definition that went with the enumerated list of pool types:   The type of pool for a pool backed security. Each of these pool types represents pools of mortgages that have conformed to certain standards (that change periodically) that make them "conforming" -- such as mortgage balance under a certain threshold, creditworthiness, loan-to-value, etc.  Further Notes: Non Agency signifies a tranched security, for which there will also be a Tranche Type for the security tranche itself. All other pool types are Agency pool types.   List Populated from Cutter document Page 5.   Additional terms from Adept Advistory: Under Agency mortgages, basically you have various types of pools under the various agencies. You have: -GNMA-I -GNMA-II -GNMA Platinum -FNMA  -FHLMC -FHLMC Gold As far as definitions:The simple definition is that each of these pool types represents pools of mortgages that have conformed to certain standards (that change periodically) that make them "conforming" -- such as mortgage balance under a certain threshold, creditworthiness, loan-to-value, etc. Also, GNMA is explicitly backed by the US government, while FNMA and FHLMC are only implicitly backed by the US government. Perhaps there needs to be some research done on the parameters for what makes a loan conforming or not.   Consensus:Review.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
